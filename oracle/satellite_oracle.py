import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class SatelliteOracle:
    def __init__(self):
        self.model = GPT2LMHeadModel.from_pretrained("gpt2").eval()
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    def forecast(self, prompt):
        inputs = self.tokenizer.encode(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=50, do_sample=True)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)