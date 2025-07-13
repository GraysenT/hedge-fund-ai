def load_codex(filepath="memory/intelligence_codex.md"):
    if not os.path.exists(filepath):
        return "⚠️ Codex is empty or missing."
    with open(filepath, "r") as f:
        return f.read()