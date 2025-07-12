```python
def deep_recursive_function(data, depth=0):
    # Define a maximum depth to prevent too deep recursion
    MAX_DEPTH = 100

    # Check if the maximum recursion depth has been reached
    if depth > MAX_DEPTH:
        print("Max recursion depth reached, backing out.")
        return None

    # Base case: if data meets a certain condition, stop recursion
    if data == 0:  # Example condition
        return "Base case reached"

    # Recursive case: modify data and recurse deeper
    try:
        result = deep_recursive_function(data - 1, depth + 1)
        return result
    except RecursionError:
        print("Recursion error caught, backing out.")
        return None

# Example usage
result = deep_recursive_function(105)
print("Result:", result)
```