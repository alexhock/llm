from datasets import load_dataset


def prepare_dataset(output_dir):
    # Convert dataset to OAI messages
    system_message = """You are an text to SQL query translator. Users will ask you questions in English and you will generate a SQL query based on the provided SCHEMA.
    SCHEMA:
    {schema}"""

    def create_conversation(sample):
        return {
            "messages": [
                {"role": "system", "content": system_message.format(schema=sample["context"])},
                {"role": "user", "content": sample["question"]},
                {"role": "assistant", "content": sample["answer"]},
            ]
        }

    # Load dataset from the hub
    dataset = load_dataset("b-mc2/sql-create-context", split="train")
    dataset = dataset.shuffle().select(range(12500))

    # Convert dataset to OAI messages
    dataset = dataset.map(create_conversation, remove_columns=dataset.features, batched=False)
    # split dataset into 10,000 training samples and 2,500 test samples
    dataset = dataset.train_test_split(test_size=2500 / 12500)

    print(dataset["train"][345]["messages"])

    # save datasets to disk
    dataset["train"].to_json(f"{output_dir}/train_dataset.json", orient="records")
    dataset["test"].to_json(f"{output_dir}/test_dataset.json", orient="records")

    return dataset


if __name__ == "__main__":
    prepare_dataset("./")