```python
def safe_recursive_function(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if wrapper.depth > wrapper.max_depth:
            raise RecursionError("Maximum recursion depth exceeded")
        wrapper.depth += 1
        try:
            result = func(*args, **kwargs)
        finally:
            wrapper.depth -= 1
        return result
    wrapper.max_depth = 1000  # Set maximum depth to a safe limit
    wrapper.depth = 0
    return wrapper

@safe_recursive_function
def factorial(n):
    if n in (0, 1):
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
try:
    print(factorial(5))  # Should print 120
    print(factorial(1000))  # Should raise a RecursionError
except RecursionError as e:
    print(e)
```