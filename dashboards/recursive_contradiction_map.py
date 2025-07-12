Here's a Python script that can help identify and highlight contradicting logic loops in a given set of Python functions. The script uses static analysis to parse Python code, identify loops, and check for logical contradictions within those loops. This example uses the `ast` module to parse the abstract syntax tree (AST) of the code and then analyzes the conditions within loops for contradictions.

```python
import ast

class ContradictionFinder(ast.NodeVisitor):
    def __init__(self):
        self.current_loop = None
        self.loops_with_contradictions = []

    def visit_While(self, node):
        self.current_loop = node
        self.generic_visit(node)
        self.current_loop = None

    def visit_For(self, node):
        self.current_loop = node
        self.generic_visit(node)
        self.current_loop = None

    def visit_If(self, node):
        if self.current_loop:
            if self.is_contradictory(node):
                self.loops_with_contradictions.append((self.current_loop, node))
        self.generic_visit(node)

    def is_contradictory(self, node):
        # This is a simplified contradiction checker
        # Real implementation would require complex logical analysis
        if isinstance(node.test, ast.Compare):
            if isinstance(node.test.ops[0], (ast.Eq, ast.NotEq, ast.Is, ast.IsNot)):
                left = self.get_constant_value(node.test.left)
                right = self.get_constant_value(node.test.comparators[0])
                if left is not None and right is not None:
                    if isinstance(node.test.ops[0], (ast.Eq, ast.Is)) and left != right:
                        return True
                    elif isinstance(node.test.ops[0], (ast.NotEq, ast.IsNot)) and left == right:
                        return True
        return False

    def get_constant_value(self, node):
        if isinstance(node, ast.Constant):
            return node.value
        return None

def find_contradictions_in_code(code):
    tree = ast.parse(code)
    finder = ContradictionFinder()
    finder.visit(tree)
    return finder.loops_with_contradictions

# Example Python code with a potential contradiction
code = """
for i in range(10):
    if i == 5:
        continue
    elif i == 5:
        break
"""

contradictions = find_contradictions_in_code(code)
for loop, contradiction in contradictions:
    print(f"Contradiction found in loop starting at line {loop.lineno} and contradiction at line {contradiction.lineno}")
```

This script defines a class `ContradictionFinder` that extends `ast.NodeVisitor` to traverse the AST of the provided code. It checks for contradictions specifically in conditional statements within loops (`for` and `while`). The contradiction detection is currently simplistic, focusing on direct equality and inequality comparisons involving constants. This can be expanded with more sophisticated logical analysis as needed.

The `find_contradictions_in_code` function parses the code into an AST, uses the `ContradictionFinder` to visit nodes, and then reports any found contradictions, including their locations in the source code.