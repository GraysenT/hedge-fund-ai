from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
from datasets import load_dataset

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

ds = load_dataset("json", data_files="logs/dreams.jsonl")

def tokenize(example):
    return tokenizer(example["context"], padding="max_length", truncation=True)

tokenized = ds.map(tokenize, batched=True)

trainer = Trainer(
    model=model,
    args=TrainingArguments(
        output_dir="oracle_model",
        per_device_train_batch_size=2,
        num_train_epochs=2,
        logging_dir="oracle_logs"
    ),
    train_dataset=tokenized["train"]
)

trainer.train()