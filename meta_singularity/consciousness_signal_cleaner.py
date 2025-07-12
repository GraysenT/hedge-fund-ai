```python
def filter_recursion(signal, threshold=0.1):
    """
    Filters out recursion in a signal to preserve only coherent, original signals.
    
    Args:
    signal (list of float): The input signal to be filtered.
    threshold (float): The threshold value to determine the similarity that leads to filtering.

    Returns:
    list of float: The filtered signal.
    """
    if len(signal) < 2:
        return signal

    filtered_signal = [signal[0]]  # Start with the first element of the signal

    for i in range(1, len(signal)):
        # Calculate the difference between the current signal value and the last added value in filtered_signal
        if abs(signal[i] - filtered_signal[-1]) > threshold:
            filtered_signal.append(signal[i])

    return filtered_signal

# Example usage:
input_signal = [0.1, 0.12, 0.11, 0.5, 0.51, 1.0, 1.02, 1.5, 1.52, 2.0]
output_signal = filter_recursion(input_signal)
print(output_signal)
```