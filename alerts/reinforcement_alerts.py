```python
import numpy as np
import matplotlib.pyplot as plt

def plot_strategy_adjustments(strategy_weights):
    """
    Plots the strategy weights over reinforcement rounds to highlight heavy adjustments.

    Parameters:
    - strategy_weights: A list of numpy arrays where each array represents the strategy weights at a given round.

    Returns:
    None, but displays a matplotlib plot.
    """
    num_rounds = len(strategy_weights)
    num_strategies = len(strategy_weights[0])
    
    # Calculate changes in strategy weights
    weight_changes = [np.abs(strategy_weights[i] - strategy_weights[i-1]) for i in range(1, num_rounds)]
    
    # Identify heavy adjustments (greater than a threshold)
    threshold = 0.5  # Define threshold for heavy adjustments
    heavy_adjustments = [change > threshold for change in weight_changes]
    
    # Plotting
    plt.figure(figsize=(10, 6))
    
    for strategy_index in range(num_strategies):
        changes_for_strategy = [change[strategy_index] for change in weight_changes]
        rounds = np.arange(1, num_rounds)
        
        # Plot all changes
        plt.plot(rounds, changes_for_strategy, label=f'Strategy {strategy_index + 1}')
        
        # Highlight heavy adjustments
        heavy_rounds = rounds[heavy_adjustments[strategy_index]]
        heavy_changes = np.array(changes_for_strategy)[heavy_adjustments[strategy_index]]
        plt.scatter(heavy_rounds, heavy_changes, color='red', s=50, zorder=5)
    
    plt.title('Strategy Weight Adjustments Over Rounds')
    plt.xlabel('Round')
    plt.ylabel('Weight Change')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
strategy_weights = [
    np.array([0.2, 0.3, 0.5]),
    np.array([0.1, 0.6, 0.3]),
    np.array([0.15, 0.65, 0.2]),
    np.array([0.1, 0.8, 0.1])
]

plot_strategy_adjustments(strategy_weights)
```