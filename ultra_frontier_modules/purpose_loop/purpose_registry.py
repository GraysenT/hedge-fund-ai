import json
import os

PURPOSE_FILE = "memory/purpose_registry.json"

def save_purpose(profile):
    os.makedirs("memory", exist_ok=True)
    data = profile.__dict__.copy()
    data["history"] = profile.history
    with open(PURPOSE_FILE, "w") as f:
        json.dump(data, f, indent=2)

def load_purpose():
    if not os.path.exists(PURPOSE_FILE):
        return None
    from .purpose_profile import PurposeProfile
    with open(PURPOSE_FILE, "r") as f:
        data = json.load(f)
    p = PurposeProfile(data["name"], data["core_directive"], data["intent_score"])
    p.id = data["id"]
    p.created = data["created"]
    p.history = data.get("history", [])
    return p