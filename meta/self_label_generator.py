```python
def generate_tags(depth):
    if depth == 0:
        return ["base_case"]
    else:
        previous_tags = generate_tags(depth - 1)
        current_tag = f"recursion_depth_{depth}"
        return previous_tags + [current_tag]

# Example usage
depth = 5
tags = generate_tags(depth)
print(tags)
```