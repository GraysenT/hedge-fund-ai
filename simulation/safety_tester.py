```python
import ast
from pylint import epylint as lint
import subprocess
import sys

def validate_python_code(code):
    """
    Validates Python code for syntax, logic, and security risks before deployment.
    
    Args:
    code (str): The Python code to validate.
    
    Returns:
    bool: True if the code is valid, False otherwise.
    str: Validation messages or error details.
    """
    try:
        # Check for syntax errors first
        ast.parse(code)
    except SyntaxError as e:
        return False, f"Syntax error in code: {e}"
    
    # Save the code to a temporary file
    with open('temp_code.py', 'w') as f:
        f.write(code)
    
    # Use pylint to check for additional issues
    (pylint_stdout, pylint_stderr) = lint.py_run('temp_code.py', return_std=True)
    pylint_output = pylint_stdout.getvalue()
    
    # Check for critical issues or errors in pylint output
    if "error" in pylint_output.lower() or "fatal" in pylint_output.lower():
        return False, f"Pylint reported critical issues: {pylint_output}"
    
    # Optionally, run the code in a sandboxed environment (e.g., Docker) to check for runtime issues
    # This is a placeholder for actual sandbox testing logic
    try:
        result = subprocess.run(['python', 'temp_code.py'], capture_output=True, text=True, timeout=5)
        if result.returncode != 0:
            return False, f"Runtime error or exception: {result.stderr}"
    except subprocess.TimeoutExpired:
        return False, "Code execution timed out, potential infinite loop or heavy processing."
    
    # Clean up the temporary file
    subprocess.run(['rm', 'temp_code.py'])
    
    return True, "Code validation passed successfully."

# Example usage
code_to_test = """
import numpy as np

def calculate_statistics(data):
    mean = np.mean(data)
    median = np.median(data)
    return mean, median

data_points = [1, 2, 3, 4, 5]
mean, median = calculate_statistics(data_points)
print(f"Mean: {mean}, Median: {median}")
"""

valid, message = validate_python_code(code_to_test)
print("Is the code valid?", valid)
print("Validation message:", message)
```