import json
from datetime import datetime

REGISTRY = "federation/node_registry.json"

def register_node(name, pubkey):
    registry = json.load(open(REGISTRY)) if os.path.exists(REGISTRY) else {}
    registry[name] = {
        "public_key": pubkey,
        "status": "active",
        "added": datetime.now().isoformat(),
        "trust": 1.0
    }
    with open(REGISTRY, "w") as f:
        json.dump(registry, f, indent=2)
    print(f"🔐 Node {name} registered.")

def list_nodes():
    registry = json.load(open(REGISTRY))
    print("🧩 Trusted Federation Nodes:")
    for name, data in registry.items():
        print(f"{name} → {data['status']} (Trust: {data['trust']})")

if __name__ == "__main__":
    register_node("node_alpha", "ssh-ed25519 AAAAC3...")
    list_nodes()