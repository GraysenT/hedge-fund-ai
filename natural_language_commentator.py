```python
def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    The factorial of a number is the product of all positive integers less than or equal to that number.
    For example, factorial of 5 (denoted as 5!) is 5 * 4 * 3 * 2 * 1 = 120.

    Args:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the number n.
    """
    # Base case: if n is 0 or 1, the factorial is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Example usage:
result = factorial(5)
print("Factorial of 5 is:", result)
```