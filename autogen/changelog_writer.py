import os
from datetime import datetime

CHANGELOG = "logs/gpt_phase_changelog.md"

def write_changelog(phase, modules):
    os.makedirs("logs", exist_ok=True)
    with open(CHANGELOG, "a") as f:
        f.write(f"\n\n## ✅ Phase {phase['id']}: {phase['title']} ({datetime.now().isoformat()})\n")
        f.write(f"**Description**: {phase['description']}\n")
        f.write(f"**Modules Generated**:\n")
        for m in modules:
            f.write(f"- `{m['path']}`\n")