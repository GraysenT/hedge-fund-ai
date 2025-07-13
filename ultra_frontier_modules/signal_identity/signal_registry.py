import os
import json

REGISTRY_PATH = "memory/signal_registry.json"

def load_registry():
    if not os.path.exists(REGISTRY_PATH):
        return []
    with open(REGISTRY_PATH, "r") as f:
        return json.load(f)

def save_registry(registry):
    with open(REGISTRY_PATH, "w") as f:
        json.dump(registry, f, indent=2)

def register_signal(entity):
    registry = load_registry()
    registry.append(entity.serialize())
    save_registry(registry)