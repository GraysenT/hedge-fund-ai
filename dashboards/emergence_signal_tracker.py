```python
import ast
import inspect

class UnexpectedBehaviorChecker(ast.NodeVisitor):
    def __init__(self, allowed_functions):
        self.allowed_functions = allowed_functions
        self.issues = []

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
            if func_name not in self.allowed_functions:
                self.issues.append(f"Call to unexpected function: {func_name} at line {node.lineno}")
        self.generic_visit(node)

    def check_code(self, code):
        tree = ast.parse(code)
        self.visit(tree)
        return self.issues

def function_to_check():
    print("This is a test function.")
    sum([1, 2, 3])
    eval("2 + 2")  # This should be flagged

# List of allowed functions
allowed_functions = {'print', 'sum'}

# Get the source code of the function
source_code = inspect.getsource(function_to_check)

# Create a checker instance
checker = UnexpectedBehaviorChecker(allowed_functions)

# Check the code for unexpected behaviors
issues = checker.check_code(source_code)

# Output the issues found
for issue in issues:
    print(issue)
```