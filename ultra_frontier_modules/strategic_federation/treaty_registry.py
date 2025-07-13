import os
import json

TREATY_FILE = "memory/federation_treaties.json"

def load_treaties():
    if not os.path.exists(TREATY_FILE):
        return []
    with open(TREATY_FILE, "r") as f:
        return json.load(f)

def save_treaty(treaty_obj):
    treaties = load_treaties()
    treaties.append(treaty_obj.serialize())
    with open(TREATY_FILE, "w") as f:
        json.dump(treaties, f, indent=2)