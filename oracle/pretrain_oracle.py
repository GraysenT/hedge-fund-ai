from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_dataset

class StrategyOracle:
    def __init__(self):
        self.model = AutoModelForCausalLM.from_pretrained("gpt2")
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2")

    def train_on_logs(self, path="logs/strategy_text.json"):
        data = load_dataset("json", data_files=path)
        tokenized = data.map(lambda e: self.tokenizer(e["text"], truncation=True, padding="max_length"), batched=True)
        args = TrainingArguments(output_dir="./oracle", per_device_train_batch_size=4, num_train_epochs=1)
        trainer = Trainer(model=self.model, args=args, train_dataset=tokenized["train"])
        trainer.train()