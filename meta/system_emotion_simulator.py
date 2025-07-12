Here's a Python script that simulates emotion-like metrics such as regret, confusion, and confidence for a decision-making scenario. The script uses random values to simulate how these metrics might change over time or in response to different decisions.

```python
import random

class EmotionSimulator:
    def __init__(self):
        self.regret = 0
        self.confusion = 0
        self.confidence = 100  # Starting with full confidence

    def make_decision(self):
        # Simulate making a decision with a random outcome
        outcome = random.choice(['success', 'failure'])
        self.update_emotions(outcome)

    def update_emotions(self, outcome):
        if outcome == 'success':
            self.regret -= random.randint(0, 5)  # Decrease regret if successful
            self.confusion -= random.randint(0, 10)  # Decrease confusion if successful
            self.confidence += random.randint(5, 15)  # Increase confidence if successful
        else:
            self.regret += random.randint(5, 15)  # Increase regret if failure
            self.confusion += random.randint(5, 20)  # Increase confusion if failure
            self.confidence -= random.randint(10, 20)  # Decrease confidence if failure

        # Ensure metrics stay within logical boundaries
        self.regret = max(0, self.regret)
        self.confusion = max(0, self.confusion)
        self.confidence = min(max(0, self.confidence), 100)

    def display_emotions(self):
        print(f"Regret: {self.regret}")
        print(f"Confusion: {self.confusion}")
        print(f"Confidence: {self.confidence}")

def main():
    simulator = EmotionSimulator()

    # Simulate a series of decisions
    for _ in range(10):
        simulator.make_decision()
        simulator.display_emotions()

if __name__ == "__main__":
    main()
```

This script defines a class `EmotionSimulator` that tracks and updates the metrics of regret, confusion, and confidence based on random outcomes of decisions. The `make_decision` method simulates a decision with a random outcome (either "success" or "failure"), and `update_emotions` adjusts the emotional metrics based on the outcome. The `display_emotions` method prints the current state of each metric.

You can run this script to see how these emotion-like metrics might evolve over a series of decisions. Adjust the ranges and probabilities to simulate different scenarios or decision-making styles.