import random

class LinguisticAgent:
    def __init__(self, name):
        self.name = name
        self.vocab = {"buy": "B", "sell": "S", "hold": "H"}
        self.experience = []

    def encode_signal(self, signal):
        return self.vocab.get(signal, "?")

    def mutate_language(self):
        swaps = [("B", "BUY"), ("S", "SELL"), ("H", "HOLD")]
        if random.random() < 0.5:
            k, v = random.choice(swaps)
            self.vocab[random.choice(list(self.vocab.keys()))] = v
            print(f"🗣 {self.name} evolved language: {self.vocab}")