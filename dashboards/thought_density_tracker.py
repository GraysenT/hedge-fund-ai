Below is a Python example that demonstrates how to track the number of recursive calls in a function. This example uses a simple recursive function to calculate the factorial of a number. The code includes a decorator that counts and prints the number of recursive calls for any function it decorates.

```python
def recursive_call_counter(func):
    """ Decorator to count and report the number of recursive calls for the decorated function. """
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        result = func(*args, **kwargs)
        return result
    wrapper.calls = 0
    return wrapper

@recursive_call_counter
def factorial(n):
    """ Recursive function to calculate the factorial of a number. """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
n = 5
result = factorial(n)
print(f"Factorial of {n} is {result}")
print(f"Number of recursive calls: {factorial.calls}")
```

This code defines a decorator `recursive_call_counter` that wraps any function to track its recursive calls. The `factorial` function is decorated with this, and each time it is called recursively, the count is incremented. After computing the factorial, the total number of calls is printed. Adjust `n` to test with different values.