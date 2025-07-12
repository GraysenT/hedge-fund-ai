```python
def calculate_system_utility(alpha, alignment, coherence, continuity):
    """
    Calculate the total system utility based on the provided parameters.
    
    Parameters:
    alpha (float): Weight factor for alignment in the utility calculation.
    alignment (float): Measure of system's alignment with goals (0 to 1).
    coherence (float): Measure of system's internal coherence (0 to 1).
    continuity (float): Measure of system's continuity over time (0 to 1).
    
    Returns:
    float: Total system utility.
    """
    # Validate input ranges
    if not (0 <= alignment <= 1 and 0 <= coherence <= 1 and 0 <= continuity <= 1):
        raise ValueError("Alignment, coherence, and continuity must be between 0 and 1.")
    
    # Calculate utility
    utility = alpha * alignment + (1 - alpha) * (coherence + continuity) / 2
    return utility

# Example usage:
alpha = 0.5
alignment = 0.8
coherence = 0.9
continuity = 0.7
utility = calculate_system_utility(alpha, alignment, coherence, continuity)
print(f"Total System Utility: {utility:.2f}")
```