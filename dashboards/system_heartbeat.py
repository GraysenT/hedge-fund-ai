Here's a Python code that demonstrates core functions, recursion, feedback, and stability through a simple example of calculating the factorial of a number using recursion. The code also includes feedback to the user about the process and checks for stability by ensuring that the input is a non-negative integer.

```python
def factorial(n):
    """
    Recursive function to calculate the factorial of a non-negative integer n.
    """
    # Stability check: Ensure n is a non-negative integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Base case: the factorial of 0 is 1
    if n == 0:
        return 1
    
    # Recursive case: n * factorial of (n-1)
    return n * factorial(n - 1)

def main():
    try:
        # User input with feedback
        n = int(input("Enter a non-negative integer to calculate its factorial: "))
        result = factorial(n)
        print(f"The factorial of {n} is {result}.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

This script defines a `factorial` function that uses recursion to compute the factorial of a given number. The `main` function handles user input and provides feedback, ensuring that the input is appropriate for the factorial function. The stability of the system is maintained by checking that the input is a non-negative integer, and feedback is provided in case of an error.