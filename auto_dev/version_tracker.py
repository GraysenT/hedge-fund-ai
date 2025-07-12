import json
import datetime

REGISTRY_PATH = "auto_dev/code_registry.json"

def log_new_strategy(name, code, metadata=None):
    with open(REGISTRY_PATH, "r") as f:
        reg = json.load(f)

    entry = {
        "name": name,
        "created": datetime.datetime.utcnow().isoformat(),
        "metadata": metadata or {}
    }

    reg["registry"].append(entry)
    reg["last_updated"] = entry["created"]

    with open(REGISTRY_PATH, "w") as f:
        json.dump(reg, f, indent=2)