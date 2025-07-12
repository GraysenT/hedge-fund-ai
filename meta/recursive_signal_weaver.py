```python
def recursive_signal_thread(input_value, output_value, reinforcement, depth):
    if depth == 0:
        return output_value
    else:
        new_input = input_value + reinforcement
        new_output = output_value + new_input
        return recursive_signal_thread(new_input, new_output, reinforcement, depth - 1)

# Example usage
input_value = 1
output_value = 1
reinforcement = 2
depth = 5
result = recursive_signal_thread(input_value, output_value, reinforcement, depth)
print("Result:", result)
```