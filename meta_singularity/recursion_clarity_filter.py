```python
def filter_noisy_loops(signal_data, threshold=0.5):
    """
    Filters out noisy recursive loops in a list of signal data to preserve core logic signals.
    
    Parameters:
        signal_data (list of float): The input signal data to be filtered.
        threshold (float): The threshold value used to determine which signals are considered noise.
    
    Returns:
        list of float: The filtered signal data.
    """
    filtered_data = []
    for i in range(1, len(signal_data)):
        if abs(signal_data[i] - signal_data[i-1]) > threshold:
            filtered_data.append(signal_data[i])
    return filtered_data

# Example usage:
input_signals = [0.1, 0.2, 0.3, 0.5, 0.8, 0.1, 0.2, 0.3, 0.5, 0.8]
filtered_signals = filter_noisy_loops(input_signals, 0.2)
print(filtered_signals)
```