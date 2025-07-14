from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
from datasets import load_dataset

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

dataset = load_dataset("json", data_files="logs/brain.jsonl")

def format_record(record):
    return {"text": f"Dream: {record['dream']}\nOracle: {record['oracle']}"}

formatted = dataset["train"].map(format_record)
tokenized = formatted.map(lambda e: tokenizer(e["text"], truncation=True, padding="max_length"), batched=True)

trainer = Trainer(
    model=model,
    args=TrainingArguments(
        output_dir="oracle_model",
        num_train_epochs=2,
        per_device_train_batch_size=2,
        logging_dir="oracle_logs",
    ),
    train_dataset=tokenized
)

trainer.train()