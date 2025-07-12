Below is a Python code example that demonstrates how to evaluate the alignment of strategies to system purpose, ethics, and logic contracts. This example uses a simple scoring system to evaluate each strategy based on predefined criteria for purpose, ethics, and logic.

```python
class Strategy:
    def __init__(self, name, purpose_score, ethics_score, logic_score):
        self.name = name
        self.purpose_score = purpose_score
        self.ethics_score = ethics_score
        self.logic_score = logic_score

    def total_score(self):
        return self.purpose_score + self.ethics_score + self.logic_score

def evaluate_strategies(strategies):
    print("Evaluating Strategies:")
    for strategy in strategies:
        print(f"Strategy: {strategy.name}")
        print(f"  Purpose Alignment Score: {strategy.purpose_score}")
        print(f"  Ethics Alignment Score: {strategy.ethics_score}")
        print(f"  Logic Alignment Score: {strategy.logic_score}")
        print(f"  Total Alignment Score: {strategy.total_score()}")
        print()

def main():
    strategies = [
        Strategy("Strategy A", purpose_score=8, ethics_score=7, logic_score=9),
        Strategy("Strategy B", purpose_score=9, ethics_score=9, logic_score=8),
        Strategy("Strategy C", purpose_score=6, ethics_score=5, logic_score=7)
    ]

    evaluate_strategies(strategies)

if __name__ == "__main__":
    main()
```

This script defines a `Strategy` class with attributes for the name of the strategy and scores for alignment with system purpose, ethics, and logic. The `total_score` method calculates the sum of these scores. The `evaluate_strategies` function prints the scores for each strategy, helping to assess how well each aligns with the desired criteria. This example can be expanded with more complex scoring mechanisms or additional criteria as needed.