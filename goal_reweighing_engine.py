Here's a Python function that rebalances goal weights across five categories: alpha, ethics, survival, growth, and trust. The function ensures that the total sum of weights equals 1 (or 100%), adjusting the weights proportionally based on their current values.

```python
def rebalance_weights(weights):
    # Calculate the total sum of the current weights
    total_weight = sum(weights.values())
    
    # Check if the total weight is zero to avoid division by zero
    if total_weight == 0:
        raise ValueError("Total weight must be greater than zero.")
    
    # Calculate new weights as a proportion of the total
    new_weights = {key: value / total_weight for key, value in weights.items()}
    
    return new_weights

# Example usage:
current_weights = {
    'alpha': 0.2,
    'ethics': 0.3,
    'survival': 0.1,
    'growth': 0.25,
    'trust': 0.15
}

new_weights = rebalance_weights(current_weights)
print("Rebalanced Weights:", new_weights)
```

This function takes a dictionary of weights, calculates their total, and then adjusts each weight to ensure the sum is exactly 1. This is useful for scenarios where the weights might have been input incorrectly or adjusted and need to be normalized.