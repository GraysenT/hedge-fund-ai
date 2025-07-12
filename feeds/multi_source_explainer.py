Below is a Python code example that calculates and explains what percent of a signal's weight came from various input sources. This example assumes that the signal is a linear combination of several input sources, and the weights are known. The code calculates the percentage contribution of each input source to the final signal.

```python
def calculate_percent_contributions(weights):
    """
    Calculate the percentage contribution of each input source based on the weights.
    
    :param weights: List or array of weights indicating the contribution of each input source to the signal.
    :return: Dictionary with input source index and its percentage contribution.
    """
    total_weight = sum(weights)
    if total_weight == 0:
        return {i: 0 for i in range(len(weights))}
    
    percent_contributions = {i: (weight / total_weight) * 100 for i, weight in enumerate(weights)}
    return percent_contributions

def explain_contributions(percent_contributions):
    """
    Generate an explanation of what percent of a signal's weight came from each input source.
    
    :param percent_contributions: Dictionary with input source index and its percentage contribution.
    :return: None
    """
    for source_index, percent in percent_contributions.items():
        print(f"Input Source {source_index + 1}: {percent:.2f}% of the signal's weight")

# Example usage
weights = [10, 20, 30, 40]  # Example weights for 4 different input sources
percent_contributions = calculate_percent_contributions(weights)
explain_contributions(percent_contributions)
```

This code defines two functions:
1. `calculate_percent_contributions`: This function takes a list of weights and returns a dictionary where each key is the index of the input source and the value is the percentage contribution of that source to the total signal.
2. `explain_contributions`: This function takes the dictionary returned by `calculate_percent_contributions` and prints an explanation of the percentage contributions.

You can modify the `weights` list in the example usage to reflect the actual weights of your input sources.