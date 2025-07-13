import json
import os

POLICY_FILE = "memory/sovereign_policies.json"

def save_policy(policy):
    os.makedirs("memory", exist_ok=True)
    policies = load_policies()
    policies.append(policy)
    with open(POLICY_FILE, "w") as f:
        json.dump(policies, f, indent=2)

def load_policies():
    if not os.path.exists(POLICY_FILE):
        return []
    with open(POLICY_FILE, "r") as f:
        return json.load(f)