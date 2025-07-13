import os
import json

REGISTRY_FILE = "memory/operator_requests.json"

def load_requests():
    if not os.path.exists(REGISTRY_FILE):
        return []
    with open(REGISTRY_FILE, "r") as f:
        return json.load(f)

def save_request(entry):
    registry = load_requests()
    registry.append(entry)
    with open(REGISTRY_FILE, "w") as f:
        json.dump(registry, f, indent=2)