import json
from pathlib import Path

OVERRIDE_PATH = Path("memory/system_overrides.json")

def set_override(key, value):
    overrides = load_overrides()
    overrides[key] = value
    with open(OVERRIDE_PATH, "w") as f:
        json.dump(overrides, f, indent=2)

def load_overrides():
    if OVERRIDE_PATH.exists():
        with open(OVERRIDE_PATH, "r") as f:
            return json.load(f)
    return {}

def get_override(key, default=None):
    return load_overrides().get(key, default)