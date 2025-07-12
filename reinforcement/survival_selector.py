```python
import numpy as np

def select_top_performers(data, top_n):
    """
    Selects the top N performing strategies from the data.

    Parameters:
        data (dict): A dictionary where keys are strategy names and values are lists of performance scores across epochs.
        top_n (int): Number of top performers to select.

    Returns:
        dict: A dictionary containing only the top N performers.
    """
    # Calculate the average performance for each strategy
    average_performance = {key: np.mean(values) for key, values in data.items()}

    # Sort strategies by their average performance in descending order
    sorted_strategies = sorted(average_performance.items(), key=lambda x: x[1], reverse=True)

    # Select the top N performers
    top_performers = sorted_strategies[:top_n]

    # Create a dictionary of the top performers
    top_performers_dict = {key: data[key] for key, _ in top_performers}

    return top_performers_dict

# Example usage:
strategies = {
    "strategy1": [0.1, 0.2, 0.3],
    "strategy2": [0.4, 0.5, 0.6],
    "strategy3": [0.7, 0.8, 0.9],
    "strategy4": [0.2, 0.3, 0.1]
}

top_n = 2
top_performers = select_top_performers(strategies, top_n)
print(top_performers)
```