```python
def legacy_logic(n):
    # Example of a legacy logic function
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def modern_recursion(n):
    # Example of a modern recursion function
    if n == 0:
        return 1
    else:
        return n * modern_recursion(n - 1)

def safe_recursive_function(n):
    try:
        # Try to use modern recursion
        return modern_recursion(n)
    except RecursionError:
        # If recursion fails, fall back to legacy logic
        return legacy_logic(n)

# Example usage
n = 10
result = safe_recursive_function(n)
print(f"Factorial of {n} is {result}")
```