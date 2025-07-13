Here's a Python implementation that uses a decorator to store recent recursive function calls and their results for reuse or learning. This implementation uses a dictionary to cache results of previous calls, which can help in speeding up the function for already computed inputs by avoiding redundant calculations.

```python
import functools

def recursive_cache(func):
    cache = {}  # Cache to store function results
    history = []  # History to store sequence of calls

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Fetching from cache for args: {args}")
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            history.append((args, result))
            if len(history) > 10:  # Limit history to last 10 entries
                history.pop(0)
            return result

    wrapper.cache = cache
    wrapper.history = history
    return wrapper

@recursive_cache
def factorial(n):
    """Compute the factorial of n recursively with caching."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
print(factorial(5))  # Computes factorial of 5
print(factorial(3))  # Fetches from cache
print(factorial(6))  # Computes factorial of 6 using cached factorial(5)

# Accessing the cache and history
print("Cache:", factorial.cache)
print("History:", factorial.history)
```

This code defines a decorator `recursive_cache` which can be applied to any recursive function. It maintains a cache to store results of previous computations and a history list to keep track of recent function calls and their results. The history list is capped at the last 10 entries to prevent it from growing indefinitely.

The `factorial` function is an example of how you can use this decorator. It calculates the factorial of a number using recursion, and with the help of the decorator, it avoids redundant calculations by fetching results from the cache when possible. The example usage shows how the cache works and how you can access the cache and history.