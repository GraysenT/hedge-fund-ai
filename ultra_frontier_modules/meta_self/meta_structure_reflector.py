import os
import ast

def list_python_modules(base_dir=".", exclude_dirs=None):
    exclude_dirs = exclude_dirs or ["venv", "__pycache__", "logs", "data"]
    modules = []
    for root, dirs, files in os.walk(base_dir):
        if any(e in root for e in exclude_dirs):
            continue
        for f in files:
            if f.endswith(".py"):
                modules.append(os.path.join(root, f))
    return modules

def extract_top_level_functions(filepath):
    with open(filepath, "r") as f:
        node = ast.parse(f.read(), filename=filepath)
    return [n.name for n in node.body if isinstance(n, ast.FunctionDef)]

def summarize_structure():
    files = list_python_modules()
    structure = {}
    for f in files:
        try:
            structure[f] = extract_top_level_functions(f)
        except Exception as e:
            structure[f] = [f"⚠️ Error parsing: {e}"]
    return structure