```python
def factorial(n):
    """
    Purpose: Calculate the factorial of a given number n.
    Origin: Factorial is defined as n! = n * (n-1) * ... * 1 for n >= 1 and 1 for n = 0.
    Output Summary: Returns the factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """
    Purpose: Calculate the nth Fibonacci number.
    Origin: Fibonacci sequence is defined by F(n) = F(n-1) + F(n-2) with base cases F(0) = 0, F(1) = 1.
    Output Summary: Returns the nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def binary_search(arr, low, high, x):
    """
    Purpose: Perform a binary search to find the index of x in sorted array arr.
    Origin: Binary search algorithm divides the array into halves to reduce the search space by half each time.
    Output Summary: Returns the index of x if present in arr; otherwise, returns -1.
    """
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

def gcd(a, b):
    """
    Purpose: Find the greatest common divisor of two numbers a and b.
    Origin: GCD of two numbers is the largest number that divides both of them without leaving a remainder.
    Output Summary: Returns the greatest common divisor of a and b.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Example usage:
print("Factorial of 5:", factorial(5))
print("5th Fibonacci number:", fibonacci(5))
print("Index of 3 in [1, 2, 3, 4, 5]:", binary_search([1, 2, 3, 4, 5], 0, 4, 3))
print("GCD of 48 and 18:", gcd(48, 18))
```