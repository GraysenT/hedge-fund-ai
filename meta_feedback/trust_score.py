```python
import random

class Module:
    def __init__(self, name):
        self.name = name
        self.history_score = random.randint(0, 100)
        self.survival_score = random.randint(0, 100)
        self.interaction_score = random.randint(0, 100)

    def calculate_trust_score(self):
        # Weighing each component equally for simplicity
        return (self.history_score + self.survival_score + self.interaction_score) / 3

def main():
    modules = [
        Module("ModuleA"),
        Module("ModuleB"),
        Module("ModuleC"),
        Module("ModuleD"),
        Module("ModuleE")
    ]

    for module in modules:
        trust_score = module.calculate_trust_score()
        print(f"{module.name} Trust Score: {trust_score:.2f}")

if __name__ == "__main__":
    main()
```