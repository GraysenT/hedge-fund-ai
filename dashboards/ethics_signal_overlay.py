Below is a Python code example that demonstrates how to overlay every strategy with live ethical compliance scores. This example assumes you have a list of strategies and a function to calculate ethical compliance scores for each strategy. The scores are then displayed alongside each strategy.

```python
import random

# Example strategies
strategies = [
    "Strategy A: Invest in renewable energy",
    "Strategy B: Expand into emerging markets",
    "Strategy C: Develop new pharmaceuticals",
    "Strategy D: Increase automation in production"
]

# Function to simulate calculating an ethical compliance score
def calculate_ethical_compliance_score(strategy):
    # Random score between 0 (low compliance) and 100 (high compliance)
    return random.randint(0, 100)

# Function to overlay strategies with live ethical compliance scores
def overlay_strategies_with_scores(strategies):
    for strategy in strategies:
        score = calculate_ethical_compliance_score(strategy)
        print(f"{strategy} - Ethical Compliance Score: {score}")

# Run the function to display strategies with their ethical compliance scores
overlay_strategies_with_scores(strategies)
```

This code defines a list of strategies and a function to randomly generate an ethical compliance score for each strategy. It then prints each strategy with its corresponding ethical compliance score. In a real-world application, the function `calculate_ethical_compliance_score` would involve complex logic based on ethical guidelines and data analysis.