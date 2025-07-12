```python
def validate_logic(logic_function, test_cases):
    """
    Validates a given logic function against provided test cases.

    Parameters:
    - logic_function: a function that contains the logic to be validated.
    - test_cases: a list of tuples, where each tuple contains the input arguments as the first element
      and the expected output as the second element.

    Returns:
    - results: a list of tuples, each containing the test case input, expected output, actual output,
      and a boolean indicating if the test passed.
    """
    results = []
    for args, expected in test_cases:
        if not isinstance(args, tuple):
            args = (args,)
        actual = logic_function(*args)
        passed = actual == expected
        results.append((args, expected, actual, passed))
    return results

def example_logic(x):
    """
    Example logic function to be tested.
    """
    return x * 2

# Define test cases for the example logic
test_cases = [
    ((2,), 4),
    ((-1,), -2),
    ((0,), 0),
    ((100,), 200)
]

# Validate the logic
validation_results = validate_logic(example_logic, test_cases)

# Print the results
for test in validation_results:
    print(f"Input: {test[0]}, Expected: {test[1]}, Got: {test[2]}, Passed: {test[3]}")
```