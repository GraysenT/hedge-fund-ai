import json
import os
from datetime import datetime

VAULT = "immortal/alpha_archive.json"

def store_successful_strategy(name, logic, metadata=None):
    os.makedirs("immortal", exist_ok=True)
    entry = {
        "name": name,
        "logic": logic,
        "created": datetime.utcnow().isoformat(),
        "metadata": metadata or {}
    }

    try:
        if os.path.exists(VAULT):
            with open(VAULT, "r") as f:
                archive = json.load(f)
        else:
            archive = {"strategies": []}
        archive["strategies"].append(entry)

        with open(VAULT, "w") as f:
            json.dump(archive, f, indent=2)
    except Exception as e:
        print("[SoulVault] Error:", e)