```python
import numpy as np

class StrategyManager:
    def __init__(self, strategies, initial_trust_scores):
        """
        Initialize the StrategyManager with strategies and their corresponding initial trust scores.
        
        :param strategies: List of strategies (could be function names or any callable object)
        :param initial_trust_scores: List of initial trust scores corresponding to each strategy
        """
        self.strategies = strategies
        self.trust_scores = np.array(initial_trust_scores)
        self.decay_factor = 0.95  # Decay factor for trust scores
        self.underperformance_threshold = 0.5  # Threshold below which a strategy is considered underperforming

    def update_trust_scores(self, performance_scores):
        """
        Update trust scores based on the performance of each strategy.
        
        :param performance_scores: List of performance scores for each strategy
        """
        # Normalize performance scores
        normalized_scores = np.array(performance_scores) / np.sum(performance_scores)
        
        # Update trust scores based on performance
        self.trust_scores = self.trust_scores * self.decay_factor + normalized_scores
        
        # Further reduce trust score for underperforming strategies
        underperformance_mask = normalized_scores < self.underperformance_threshold
        self.trust_scores[underperformance_mask] *= self.decay_factor

    def select_strategy(self):
        """
        Select a strategy based on the current trust scores, using a probabilistic approach.
        
        :return: Selected strategy
        """
        # Normalize trust scores to create a probability distribution
        probabilities = self.trust_scores / np.sum(self.trust_scores)
        
        # Choose a strategy based on the probability distribution
        chosen_index = np.random.choice(len(self.strategies), p=probabilities)
        return self.strategies[chosen_index]

# Example usage
def strategy_a():
    return "Executing Strategy A"

def strategy_b():
    return "Executing Strategy B"

def strategy_c():
    return "Executing Strategy C"

# Initialize the strategy manager
strategies = [strategy_a, strategy_b, strategy_c]
initial_trust_scores = [1.0, 1.0, 1.0]
manager = StrategyManager(strategies, initial_trust_scores)

# Simulate updating trust scores based on some performance metrics
manager.update_trust_scores([0.6, 0.3, 0.1])

# Select a strategy based on updated trust scores
selected_strategy = manager.select_strategy()
print(selected_strategy())
```

This Python code defines a `StrategyManager` class that manages multiple strategies and their trust scores. Trust scores are updated based on performance scores and are decayed over time to gradually fade underperforming strategies. The manager selects a strategy probabilistically based on the current trust scores.