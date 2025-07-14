import json
import os

def log_dream(agent_id, dream):
    os.makedirs("logs/dreams", exist_ok=True)
    with open(f"logs/dreams/{agent_id}_dream.json", "a") as f:
        json.dump(dream, f, indent=2)