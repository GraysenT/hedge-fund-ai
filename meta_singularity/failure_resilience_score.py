Below is a Python script that scores modules based on resilience to failure, contradiction, and decay. The script assumes that each module is represented by a Python file and that you can evaluate the resilience by analyzing the code structure, dependencies, and error handling mechanisms.

The script will:
1. Analyze Python files in a specified directory.
2. Score each module based on:
   - Failure resilience (use of try-except blocks, logging).
   - Contradiction resilience (consistency in function returns, variable usage).
   - Decay resilience (documentation, updates, and code complexity).

```python
import os
import ast
import datetime
from radon.complexity import cc_visit
from radon.metrics import mi_visit

def analyze_module(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Parse the Python file into an AST
    tree = ast.parse(content)

    # Initialize scores
    failure_resilience = 0
    contradiction_resilience = 0
    decay_resilience = 0

    # Analyze for failure resilience: Check for try-except blocks and logging
    for node in ast.walk(tree):
        if isinstance(node, ast.Try):
            failure_resilience += 5
        elif isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
            if 'logging' in [alias.name for alias in node.names]:
                failure_resilience += 3

    # Analyze for contradiction resilience: Check for consistent return types
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            return_types = set()
            for n in ast.walk(node):
                if isinstance(n, ast.Return):
                    if n.value is None:
                        return_types.add(type(None))
                    elif isinstance(n.value, ast.Num):
                        return_types.add(float)
                    elif isinstance(n.value, ast.Str):
                        return_types.add(str)
                    # Add more types as necessary
            if len(return_types) > 1:
                contradiction_resilience -= 5
            else:
                contradiction_resilience += 5

    # Analyze for decay resilience: Check for comments, docstrings, and code complexity
    docstring_count = sum(isinstance(node, ast.Expr) and isinstance(node.value, ast.Str) for node in ast.walk(tree))
    decay_resilience += docstring_count * 2

    # Use Radon to calculate Maintainability Index
    try:
        mi_score = mi_visit(content, True)
        decay_resilience += mi_score
    except Exception as e:
        print(f"Error calculating MI for {file_path}: {e}")

    # Calculate Cyclomatic Complexity
    complexity_scores = [cc_visit(content)]
    avg_complexity = sum(score for func in complexity_scores for score in func) / len(complexity_scores)
    if avg_complexity < 5:
        decay_resilience += 5
    elif avg_complexity < 10:
        decay_resilience += 3
    else:
        decay_resilience -= 5

    return failure_resilience, contradiction_resilience, decay_resilience

def score_modules(directory):
    scores = {}
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            file_path = os.path.join(directory, filename)
            scores[filename] = analyze_module(file_path)
    return scores

# Example usage
directory_path = 'path_to_your_python_modules'
module_scores = score_modules(directory_path)
for module, scores in module_scores.items():
    print(f"{module}: Failure Resilience = {scores[0]}, Contradiction Resilience = {scores[1]}, Decay Resilience = {scores[2]}")
```

This script uses the `ast` module to parse Python code into an abstract syntax tree, which it then traverses to calculate scores based on the criteria mentioned. It also uses the `radon` library to calculate the Maintainability Index and Cyclomatic Complexity, which are indicators of code quality and complexity. Adjust the scoring logic as necessary to fit the specific needs and standards of your project.