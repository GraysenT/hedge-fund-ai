import ast

class StrategyCompiler:
    def __init__(self, text: str):
        self.text = text

    def verify(self):
        try:
            tree = ast.parse(self.text)
            return all(isinstance(n, (ast.FunctionDef, ast.Import, ast.ClassDef)) for n in tree.body)
        except Exception as e:
            return False

    def compile(self, filename="compiled_strategy.py"):
        if self.verify():
            with open(filename, "w") as f:
                f.write(self.text)
            return True
        return False