import os
from datetime import datetime

CODEX_FILE = "memory/intelligence_codex.md"

def write_codex_entry(title: str, summary: str, key_learnings: list, tags: list):
    os.makedirs("memory", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = f"""
### 🧠 {title}
**Timestamp:** {timestamp}  
**Tags:** {", ".join(tags)}

**Summary:**  
{summary}

**Key Learnings:**  
""" + "\n".join([f"- {k}" for k in key_learnings]) + "\n"

    with open(CODEX_FILE, "a") as f:
        f.write(entry + "\n")