import uuid, json, os

def create_identity():
    return {
        "id": str(uuid.uuid4()),
        "api_key": uuid.uuid4().hex,
        "mode": "sim",
        "permissions": ["read", "dream", "mutate"]
    }

def save_identity(agent_id, identity):
    with open(f"secrets/{agent_id}.json", "w") as f:
        json.dump(identity, f, indent=2)