```python
import random

class StrategyHybridizer:
    def __init__(self):
        self.failed_strategies = []

    def add_failed_strategy(self, strategy):
        """Add a failed strategy to the repository."""
        self.failed_strategies.append(strategy)

    def create_hybrid_strategy(self):
        """Create a new strategy by combining fragments of failed strategies."""
        if len(self.failed_strategies) < 2:
            raise ValueError("Not enough failed strategies to form a hybrid.")

        # Randomly select two different failed strategies
        strategy1, strategy2 = random.sample(self.failed_strategies, 2)

        # Split each strategy into parts
        midpoint1 = len(strategy1) // 2
        midpoint2 = len(strategy2) // 2

        # Create new hybrid strategies by mixing parts
        hybrid1 = strategy1[:midpoint1] + strategy2[midpoint2:]
        hybrid2 = strategy2[:midpoint2] + strategy1[midpoint1:]

        return hybrid1, hybrid2

# Example usage
if __name__ == "__main__":
    hybridizer = StrategyHybridizer()
    hybridizer.add_failed_strategy("ABCD")
    hybridizer.add_failed_strategy("WXYZ")
    hybrid1, hybrid2 = hybridizer.create_hybrid_strategy()
    print("Hybrid Strategy 1:", hybrid1)
    print("Hybrid Strategy 2:", hybrid2)
```