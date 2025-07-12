```python
import random

def strategy_one(issue):
    return f"Strategy One resolves {issue} by prioritizing immediate action."

def strategy_two(issue):
    return f"Strategy Two resolves {issue} by emphasizing careful planning and analysis."

def debate(issue):
    strategies = [strategy_one, strategy_two]
    results = []

    print(f"Debating on the issue: {issue}")
    for strategy in strategies:
        result = strategy(issue)
        results.append(result)
        print(result)

    chosen_strategy = random.choice(results)
    print(f"\nChosen strategy: {chosen_strategy}")

# Example usage
issue = "resource allocation in a project"
debate(issue)
```