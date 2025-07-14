from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments

model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

ds = load_dataset("json", data_files="logs/dreams.jsonl")
tokenized = ds.map(lambda e: tokenizer(e["context"], truncation=True, padding="max_length"), batched=True)

trainer = Trainer(
    model=model,
    args=TrainingArguments(output_dir="meta_oracle", per_device_train_batch_size=4, num_train_epochs=3),
    train_dataset=tokenized["train"]
)

trainer.train()