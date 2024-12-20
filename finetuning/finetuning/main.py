import argparse
import numpy as np
import pandas as pd
import os
from tqdm import tqdm
import bitsandbytes as bnb
import torch
from accelerate import Accelerator
from datasets import Dataset
from peft import LoraConfig, PeftConfig
from trl import SFTTrainer
import mlflow
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
    pipeline,
    logging,
)
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split


def evaluate(y_true, y_pred):
    labels = ["positive", "neutral", "negative"]
    mapping = {"positive": 2, "neutral": 1, "none": 1, "negative": 0}

    def map_func(x):
        return mapping.get(x, 1)

    y_true = np.vectorize(map_func)(y_true)
    y_pred = np.vectorize(map_func)(y_pred)

    results = {
        "accuracy": accuracy_score(y_true=y_true, y_pred=y_pred),
    }
    # Calculate accuracy
    print(f'Accuracy: {results["accuracy"]:.3f}')

    # Generate accuracy report
    unique_labels = set(y_true)  # Get unique labels

    for label in unique_labels:
        label_indices = [i for i in range(len(y_true)) if y_true[i] == label]
        label_y_true = [y_true[i] for i in label_indices]
        label_y_pred = [y_pred[i] for i in label_indices]
        accuracy = accuracy_score(label_y_true, label_y_pred)
        results["accuracy_" + str(label)] = accuracy
        print(f"Accuracy for label {label}: {accuracy:.3f}")

    # Generate classification report
    class_report = classification_report(y_true=y_true, y_pred=y_pred)
    print("\nClassification Report:")
    print(class_report)

    # Generate confusion matrix
    conf_matrix = confusion_matrix(y_true=y_true, y_pred=y_pred, labels=[0, 1, 2])
    print("\nConfusion Matrix:")
    print(conf_matrix)

    return results


def generate_prompt(data_point):
    return f"""The sentiment of the following phrase: '{data_point["text"]}' is 
            \n\n Positive
            \n Negative
            \n Neutral
            \n Cannot be determined
            \n\nSolution: The correct option is {data_point["sentiment"]}""".strip()


def generate_test_prompt(data_point):
    return f"""The sentiment of the following phrase: '{data_point["text"]}' is 
            \n\n Positive
            \n Negative
            \n Neutral
            \n Cannot be determined
            \n\nSolution: The correct option is""".strip()


def load_data(filename):
    df = pd.read_csv(
        filename, names=["sentiment", "text"], encoding="utf-8", encoding_errors="replace"
    )

    X_train = list()
    X_test = list()
    for sentiment in ["positive", "neutral", "negative"]:
        train, test = train_test_split(
            df[df.sentiment == sentiment], train_size=300, test_size=300, random_state=42
        )
        X_train.append(train)
        X_test.append(test)

    X_train = pd.concat(X_train).sample(frac=1, random_state=10)
    X_test = pd.concat(X_test)

    eval_idx = [idx for idx in df.index if idx not in list(train.index) + list(test.index)]
    X_eval = df[df.index.isin(eval_idx)]
    X_eval = X_eval.groupby("sentiment", group_keys=False).apply(
        lambda x: x.sample(n=50, random_state=10, replace=True)
    )
    X_train = X_train.reset_index(drop=True)

    return X_train, X_test, X_eval


def get_device_map():
    world_size = torch.cuda.device_count()
    device_map = "auto"
    local_rank = int(os.environ.get("LOCAL_RANK", 0))
    ddp = world_size != 1
    if ddp:
        device_map = {"": local_rank}
    return device_map


def load_model(model_name="microsoft/phi-2", use_4bit=False, use_8bit=False):
    device_map = get_device_map()

    bnb_config = None
    if use_4bit:
        compute_dtype = getattr(torch, "float16")
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=use_4bit,
            bnb_4bit_use_double_quant=False,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=compute_dtype,
        )

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        load_in_8bit=use_8bit,
        trust_remote_code=True,
        device_map=device_map,
        quantization_config=bnb_config,
    )

    model.config.use_cache = False
    model.config.pretraining_tp = 1

    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
        trust_remote_code=True,
    )
    tokenizer.pad_token = tokenizer.eos_token

    return model, tokenizer


def predict(X_test, model, tokenizer):
    y_pred = []
    for i in tqdm(range(len(X_test))):
        prompt = X_test.iloc[i]["text"]
        pipe = pipeline(
            task="text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=3,
            temperature=0.0,
        )
        result = pipe(prompt, pad_token_id=pipe.tokenizer.eos_token_id)
        answer = result[0]["generated_text"].split("The correct option is")[-1].lower()
        if "positive" in answer:
            y_pred.append("positive")
        elif "negative" in answer:
            y_pred.append("negative")
        elif "neutral" in answer:
            y_pred.append("neutral")
        else:
            y_pred.append("none")
    return y_pred


def get_trainer(args, model, tokenizer, train_data, eval_data):
    target_modules = ["q_proj", "up_proj", "o_proj", "k_proj", "down_proj", "gate_proj", "v_proj"]

    peft_config = LoraConfig(
        r=16,
        lora_alpha=16,
        target_modules=target_modules,
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )

    training_arguments = TrainingArguments(
        output_dir="output",
        num_train_epochs=args.epochs,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=8,  # 4
        optim="paged_adamw_32bit",
        save_steps=0,
        logging_steps=25,
        learning_rate=2e-4,
        weight_decay=0.001,
        fp16=True,
        bf16=False,
        max_grad_norm=0.3,
        max_steps=-1,
        warmup_ratio=0.03,
        group_by_length=True,
        lr_scheduler_type="cosine",
        # report_to="tensorboard",
        evaluation_strategy="epoch",
    )

    trainer = SFTTrainer(
        model=model,
        train_dataset=train_data,
        eval_dataset=eval_data,
        peft_config=peft_config,
        dataset_text_field="text",
        tokenizer=tokenizer,
        args=training_arguments,
        packing=False,
        max_seq_length=512,
    )

    return trainer


def add_prompt_text(X_train, X_test, X_eval):
    # apply the prompt generation function
    X_train = pd.DataFrame(X_train.apply(generate_prompt, axis=1), columns=["text"])
    X_eval = pd.DataFrame(X_eval.apply(generate_prompt, axis=1), columns=["text"])

    y_true = X_test.sentiment
    X_test = pd.DataFrame(X_test.apply(generate_test_prompt, axis=1), columns=["text"])

    return X_train, X_test, X_eval, y_true


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
    print(args)
    # https://www.kaggle.com/code/simranjeetsingh1430/microsoft-phi2-llm-fine-tuning-qlora

    # accelerate config object. Helpful for knowing if the process is the main process
    acc = Accelerator()

    # Load the csv, split and add prompts, then convert to huggingface datasets

    X_train, X_test, X_eval = load_data(args.filename)

    X_train, X_test, X_eval, y_true = add_prompt_text(X_train, X_test, X_eval)

    # Create the huggingface datasets
    train_data = Dataset.from_pandas(X_train)
    eval_data = Dataset.from_pandas(X_eval)

    model, tokenizer = load_model(model_name=args.model_name, use_4bit=args.use_4bit, use_8bit=args.use_8bit)

    print("Before finetuning")

    if acc.is_main_process:
        # eval on the base model before finetuning
        y_pred = predict(X_test, model, tokenizer)
        results = evaluate(y_true, y_pred)
        log_metrics("base model", results)

    # Fine-tune using Lora
    trainer = get_trainer(args, model, tokenizer, train_data, eval_data)
    trainer.train()
    # if acc.is_main_process:
    trainer.model.save_pretrained(f"{args.output_dir}/phi2_sentiment_model")

    print("After finetuning")
    if acc.is_main_process:
        # eval on the finetuned model
        y_pred = predict(X_test, model, tokenizer)
        results = evaluate(y_true, y_pred)
        log_metrics("finetuned", results)
        evaluation = pd.DataFrame(
            {"text": X_test["text"], "y_true": y_true, "y_pred": y_pred},
        )
        evaluation.to_csv(f"{args.output_dir}/test_predictions.csv", index=False)

    mlflow.set_tag("status", "completed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a single filename.")
    parser.add_argument(
        "--model_name",
        type=str,
        default="microsoft/phi-2",
        help="The huggingface card name of the model to use",
    )
    parser.add_argument(
        "--filename",
        type=str,
        default="../data/sentiment/all-data.csv",
        help="The name of the file to process",
    )
    parser.add_argument(
        "--output_dir", type=str, default="./outputs", help="The name of the folder to save files"
    )
    parser.add_argument("--epochs", type=int, default=1, help="Number of epochs to fine tune")
    parser.add_argument(
        "--use_8bit", type=bool, default=False, help="Whether to use 8bit quantization"
    )
    parser.add_argument(
        "--use_4bit", type=bool, default=False, help="Whether to use 4bit quantization"
    )
    args = parser.parse_args()
    set_tags(args)
    main(args)
