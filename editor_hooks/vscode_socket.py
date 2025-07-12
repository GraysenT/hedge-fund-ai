import os

def fetch_code_from_editor(filepath: str) -> str:
    """Reads code from a given file path."""
    if not os.path.exists(filepath):
        return f"❌ File not found: {filepath}"
    with open(filepath, "r") as f:
        return f.read()

def send_code_to_editor(filepath: str, content: str, backup=True):
    """Writes content to file, with optional backup."""
    if backup and os.path.exists(filepath):
        os.rename(filepath, filepath + ".bak")
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        f.write(content)
    return f"✅ Code written to: {filepath}"