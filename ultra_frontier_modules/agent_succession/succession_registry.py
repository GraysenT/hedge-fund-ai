import os
import json

REGISTRY_PATH = "memory/agent_succession_log.json"

def save_agent(agent):
    os.makedirs("memory", exist_ok=True)
    log = load_registry()
    log.append(agent.profile())
    with open(REGISTRY_PATH, "w") as f:
        json.dump(log, f, indent=2)

def load_registry():
    if not os.path.exists(REGISTRY_PATH):
        return []
    with open(REGISTRY_PATH, "r") as f:
        return json.load(f)