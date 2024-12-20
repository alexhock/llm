import argparse
import numpy as np
import pandas as pd
import os
from tqdm import tqdm
import bitsandbytes as bnb
import torch
from accelerate import Accelerator
from peft import LoraConfig, PeftConfig
from trl import SFTTrainer
import mlflow
from trl import SFTTrainer
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
)
from peft import LoraConfig, prepare_model_for_kbit_training, get_peft_model
from datasets import load_dataset
from random import randrange
from transformers import TrainingArguments


def format_instruction(sample):
    return f"""### Instruction:
Use the Input below to create an instruction, which could have been used to generate the input using an LLM.

### Input:
{sample['response']}

### Response:
{sample['instruction']}
"""


def load_base_model(model_name, use_4bit=False, use_flash_attention=False):
    # BitsAndBytesConfig int-4 config
    bnb_config = None
    if use_4bit:
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
        )

    # Load model and tokenizer
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=bnb_config,
        use_cache=False,
        use_flash_attention_2=use_flash_attention,
        device_map="auto",
    )

    model.config.pretraining_tp = 1
    model.gradient_checkpointing_enable()

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    return model, tokenizer


def prep_peft(model):
    # LoRA config based on QLoRA paper
    peft_config = LoraConfig(
        lora_alpha=16,
        lora_dropout=0.1,
        r=64,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
    )

    # prepare model for training
    model = prepare_model_for_kbit_training(model)
    model = get_peft_model(model, peft_config)

    return peft_config, model


def set_tags(args):
    for arg, value in vars(args).items():
        print(f"{arg}: {value}")
        mlflow.set_tag(arg, value)
    if args.use_4bit == False and args.use_8bit == False:
        mlflow.set_tag("use_16bit", "True")


def log_metrics(desc, results):
    for key, value in results.items():
        mlflow.log_metric(f"{desc}_{key}", value)


def main(args):
    # https://www.philschmid.de/instruction-tune-llama-2

    # Load dataset from the hub
    dataset = load_dataset("databricks/databricks-dolly-15k", split="train")

    print(f"dataset size: {len(dataset)}")
    print(dataset[randrange(len(dataset))])

    model, tokenizer = load_base_model(model_name=args.model_name, use_4bit=args.use_4bit)

    peft_config, model = prep_peft(model)

    training_args = TrainingArguments(
        output_dir=f"{args.output_dir}/training",
        num_train_epochs=args.epochs,
        per_device_train_batch_size=6 if args.use_flash_attention else 4,
        gradient_accumulation_steps=1,
        optim="paged_adamw_32bit",
        logging_steps=10,
        save_strategy="epoch",
        learning_rate=2e-4,
        fp16=True,
        # bf16=True,
        # tf32=True,
        max_grad_norm=0.3,
        warmup_ratio=0.03,
        lr_scheduler_type="constant",
        disable_tqdm=True,  # disable tqdm since with packing values are in correct
    )

    max_seq_length = 2048  # max sequence length for model and packing of the dataset

    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        peft_config=peft_config,
        max_seq_length=max_seq_length,
        tokenizer=tokenizer,
        packing=True,
        formatting_func=format_instruction,
        args=training_args,
    )

    trainer.train()

    trainer.save_model(f"{args.output_dir}/model")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a single filename.")
    parser.add_argument(
        "--model_name",
        type=str,
        default="microsoft/phi-2",
        help="The huggingface card name of the model to use",
    )
    parser.add_argument(
        "--output_dir", type=str, default="./outputs", help="The name of the folder to save files"
    )
    parser.add_argument("--epochs", type=int, default=3, help="Number of epochs to fine tune")
    parser.add_argument(
        "--use_8bit", type=bool, default=False, help="Whether to use 8bit quantization"
    )
    parser.add_argument(
        "--use_4bit", type=bool, default=False, help="Whether to use 4bit quantization"
    )
    parser.add_argument("--use_flash_attention", type=bool, default=False)
    args = parser.parse_args()
    set_tags(args)
    main(args)
