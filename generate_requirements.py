import os
import re
from collections import Counter

PROJECT_ROOT = "."
COMMON_PYTHON_PACKAGES = {
    "pandas", "numpy", "scikit-learn", "matplotlib", "yfinance",
    "requests", "aiohttp", "fastapi", "uvicorn", "sqlalchemy",
    "plotly", "beautifulsoup4", "openai", "tqdm", "joblib",
    "tensorflow", "torch", "transformers"
}

def extract_imports_from_file(filepath):
    with open(filepath, "r", errors="ignore") as f:
        lines = f.readlines()
    imports = set()
    for line in lines:
        line = line.strip()
        match = re.match(r'^(import|from) ([\w\.]+)', line)
        if match:
            imports.add(match.group(2).split('.')[0])
    return imports

all_imports = Counter()
for root, _, files in os.walk(PROJECT_ROOT):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            imports = extract_imports_from_file(file_path)
            for imp in imports:
                all_imports[imp] += 1

# Filter known packages
needed = sorted(COMMON_PYTHON_PACKAGES & set(all_imports))

with open("requirements.txt", "w") as f:
    for pkg in needed:
        f.write(f"{pkg}\n")

print("✅ requirements.txt generated with:", needed)