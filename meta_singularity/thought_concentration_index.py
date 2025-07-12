Here's a Python script that scores how concentrated or distributed recursive logic loops are within a given Python code file. The script uses the `ast` module to parse the Python code and analyze the distribution of recursive functions. The score is calculated based on the number of recursive calls relative to the total number of function calls.

```python
import ast
import sys

class RecursionAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.functions = {}
        self.recursive_calls = {}
        self.total_calls = 0

    def visit_FunctionDef(self, node):
        self.current_function = node.name
        self.functions[node.name] = {
            'calls': [],
            'is_recursive': False
        }
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
            self.functions[self.current_function]['calls'].append(func_name)
            if func_name == self.current_function:
                self.functions[self.current_function]['is_recursive'] = True
                if func_name in self.recursive_calls:
                    self.recursive_calls[func_name] += 1
                else:
                    self.recursive_calls[func_name] = 1
            self.total_calls += 1
        self.generic_visit(node)

def calculate_concentration_score(recursive_calls, total_calls):
    if total_calls == 0:
        return 0
    return sum(recursive_calls.values()) / total_calls

def analyze_code(code):
    tree = ast.parse(code)
    analyzer = RecursionAnalyzer()
    analyzer.visit(tree)
    score = calculate_concentration_score(analyzer.recursive_calls, analyzer.total_calls)
    return score

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, "r") as file:
        code = file.read()

    score = analyze_code(code)
    print(f"Recursion Concentration Score: {score:.2f}")
```

### How to Use the Script
1. Save the script to a file, for example, `recursion_analysis.py`.
2. Run the script from the command line, passing the Python file you want to analyze as an argument:
   ```
   python recursion_analysis.py your_script.py
   ```

### Explanation
- The script reads a Python file and parses its AST.
- It identifies all function definitions and function calls.
- It checks for recursive calls (where a function calls itself).
- It calculates a "concentration score" based on the ratio of recursive calls to total function calls in the script. This score indicates how concentrated the recursion is in the overall function call structure of the code.