```python
def recursive_function(data, depth):
    if depth == 0:
        return data
    else:
        modified_data = data + 1  # Example modification to data
        print(f"Depth {depth}: {modified_data}")  # Introspection: log current depth and data
        return recursive_function(modified_data, depth - 1)

# Example usage
initial_data = 0
max_depth = 5
result = recursive_function(initial_data, max_depth)
print("Final result:", result)
```