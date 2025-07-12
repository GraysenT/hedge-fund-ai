```python
def preserve_core_identity(original_function):
    def wrapper(*args, **kwargs):
        try:
            result = original_function(*args, **kwargs)
        except RecursionError:
            print("Recursive instability detected. Halting recursion.")
            return None
        except Exception as e:
            print(f"Mutation in process detected: {e}. Attempting to preserve core functionality.")
            return None
        return result
    return wrapper

@preserve_core_identity
def recursive_function(n):
    if n == 0:
        return 1
    else:
        return n * recursive_function(n - 1)

# Example usage
print(recursive_function(5))  # Expected normal factorial result: 120
print(recursive_function(1000))  # This will likely cause a RecursionError without the decorator
```