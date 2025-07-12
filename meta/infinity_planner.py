```python
def recursive_infinite_expansion(depth=0):
    """
    This function demonstrates an infinite recursive logic expansion.
    It will keep calling itself with an incremented depth until a stack overflow occurs.
    """
    print(f"Recursion depth: {depth}")
    recursive_infinite_expansion(depth + 1)

def synthetic_test():
    """
    This function tests the recursive function to see how deep it can go before failing.
    """
    try:
        recursive_infinite_expansion()
    except RecursionError as e:
        print(f"Recursion error reached: {str(e)}")

if __name__ == "__main__":
    synthetic_test()
```