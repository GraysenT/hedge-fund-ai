```python
def reverse_string(input_string):
    """
    Reverses the given string.
    
    Args:
    input_string (str): The string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    return input_string[::-1]

# Example usage:
original_string = "Hello, world!"
reversed_string = reverse_string(original_string)
print("Original:", original_string)
print("Reversed:", reversed_string)
```