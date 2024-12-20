import argparse
import mlflow
import os
from datasets import load_dataset
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from trl import setup_chat_format
from peft import LoraConfig
from transformers import TrainingArguments
from trl import SFTTrainer
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


def set_tags(args):
    for arg, value in vars(args).items():
        print(f"{arg}: {value}")
        mlflow.set_tag(arg, value)


def log_metrics(desc, results):
    for key, value in results.items():
        mlflow.log_metric(f"{desc}_{key}", value)


def get_device_map():
    world_size = torch.cuda.device_count()
    device_map = "auto"
    local_rank = int(os.environ.get("LOCAL_RANK", 0))
    if world_size != 1:
        device_map = {"": local_rank}
    return device_map


def load_secrets_from_kv():

    hub_token = os.environ.get("HUB-TOKEN", None)
    if hub_token:
        return hub_token

    # Using Azure OpenAI this time so set the environment variables
    key_vault_name = os.environ["KEY_VAULT_NAME"]
    kv_uri = f"https://{key_vault_name}.vault.azure.net"

    credential = DefaultAzureCredential()
    kv_client = SecretClient(vault_url=kv_uri, credential=credential)
    hub_token =  kv_client.get_secret("HUB-TOKEN").value

    return hub_token


def main(args):
    # https://github.com/philschmid/deep-learning-pytorch-huggingface/blob/main/training/fine-tune-llms-in-2024-with-trl.ipynb
    
    # Get the huggingface token from env vars or keyvault.
    hub_token = load_secrets_from_kv()

    # Load jsonl data from disk
    dataset = load_dataset("json", data_files=f"train_dataset.json", split="train")

    # BitsAndBytesConfig int-4 config
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,  # switch to float16 if v100
    )

    # Load model and tokenizer
    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        device_map="auto",  # get_device_map(),
        attn_implementation="flash_attention_2",  # comment this out if v100
        torch_dtype=torch.bfloat16,  # switch to float16 if v100
        quantization_config=bnb_config,
        #force_download=True,
        #resume_download=False
    )

    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    tokenizer.padding_side = "right"  # to prevent warnings

    # # set chat template to OAI chatML, remove if you start from a fine-tuned model
    model, tokenizer = setup_chat_format(model, tokenizer)

    # LoRA config based on QLoRA paper & Sebastian Raschka experiment
    peft_config = LoraConfig(
        lora_alpha=128,
        lora_dropout=0.05,
        r=256,
        bias="none",
        target_modules="all-linear",  
        task_type="CAUSAL_LM",
    )

    args = TrainingArguments(
        output_dir=f"{args.output_dir}",  # directory to save and repository id
        num_train_epochs=args.epochs,  # number of training epochs
        per_device_train_batch_size=3,  # batch size per device during training
        gradient_accumulation_steps=2,  # number of steps before performing a backward/update pass
        gradient_checkpointing=True,  # use gradient checkpointing to save memory
        optim="adamw_torch_fused",  # use fused adamw optimizer
        logging_steps=10,  # log every 10 steps
        save_strategy="epoch",  # save checkpoint every epoch
        learning_rate=2e-4,  # learning rate, based on QLoRA paper
        bf16=True,  # use bfloat16 precision
        tf32=True,  # use tf32 precision
        max_grad_norm=0.3,  # max gradient norm based on QLoRA paper
        warmup_ratio=0.03,  # warmup ratio based on QLoRA paper
        lr_scheduler_type="constant",  # use constant learning rate scheduler
        #report_to="tensorboard",  # report metrics to tensorboard
        hub_token=hub_token
    )

    max_seq_length = 3072  # max sequence length for model and packing of the dataset

    trainer = SFTTrainer(
        model=model,
        args=args,
        train_dataset=dataset,
        peft_config=peft_config,
        max_seq_length=max_seq_length,
        tokenizer=tokenizer,
        packing=True,
        dataset_kwargs={
            "add_special_tokens": False,  # We template with special tokens
            "append_concat_token": False,  # No need to add additional separator token
        },
    )

    # start training, the model will be automatically saved to the hub and the output directory
    trainer.train()

    # save model
    print("Saving model ")
    
    trainer.save_model(f"{args.output_dir}/model")

    print("Finished")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a single filename.")
    parser.add_argument(
        "--model_name",
        type=str,
        default="Intel/neural-chat-7b-v3-3",
        help="The huggingface card name of the model to use",
    )
    parser.add_argument(
        "--output_dir", type=str, default="./outputs", help="The name of the folder to save files"
    )
    parser.add_argument("--epochs", type=int, default=3, help="Number of epochs to fine tune")
    args = parser.parse_args()
    set_tags(args)
    main(args)
