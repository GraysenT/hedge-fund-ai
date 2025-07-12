from datetime import datetime
import os

JOURNAL_PATH = "narrative/journal.log"

def log_self_reflection(thought):
    """
    Appends self-reflective thoughts and reasoning to a persistent journal.
    """
    os.makedirs("narrative", exist_ok=True)
    entry = f"\n[{datetime.utcnow().isoformat()}] {thought}\n"
    with open(JOURNAL_PATH, "a") as f:
        f.write(entry)