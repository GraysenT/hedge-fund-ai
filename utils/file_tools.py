import os

def write_file_safely(filepath: str, content: str):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        f.write(content)

def diff_preview(original: str, new: str) -> str:
    import difflib
    return "\n".join(difflib.unified_diff(
        original.splitlines(), new.splitlines(),
        lineterm="", fromfile="original", tofile="new"
    ))