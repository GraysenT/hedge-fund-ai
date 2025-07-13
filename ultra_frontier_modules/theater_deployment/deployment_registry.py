import os
import json

DEPLOYMENT_FILE = "memory/theater_deployments.json"

def save_deployment(order):
    os.makedirs("memory", exist_ok=True)
    registry = load_deployments()
    registry.append(order.serialize())
    with open(DEPLOYMENT_FILE, "w") as f:
        json.dump(registry, f, indent=2)

def load_deployments():
    if not os.path.exists(DEPLOYMENT_FILE):
        return []
    with open(DEPLOYMENT_FILE, "r") as f:
        return json.load(f)