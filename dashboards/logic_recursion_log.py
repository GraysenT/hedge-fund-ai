Here's a Python script that demonstrates a recursive function to calculate the factorial of a number. The script includes live recording of each recursive call and its result using a simple logging mechanism.

```python
def factorial(n, depth=0):
    indent = "  " * depth  # Create indentation for better visualization
    if n == 0:
        print(f"{indent}factorial(0) = 1")
        return 1
    else:
        print(f"{indent}factorial({n}) = {n} * factorial({n-1})")
        result = n * factorial(n - 1, depth + 1)
        print(f"{indent}Result of factorial({n}) = {result}")
        return result

# Example usage:
n = 5
print(f"Calculating factorial of {n}:")
factorial_result = factorial(n)
print(f"Factorial of {n} is {factorial_result}")
```

This script will output each step of the recursion, showing how the function decomposes the problem into smaller problems and then combines the results. The `depth` parameter and `indent` string are used to visually represent the depth of the recursive call stack.