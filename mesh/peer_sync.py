import requests
from worldbuilder.economy_sim import EconomySim

sim = EconomySim()

PEERS = [
    "http://127.0.0.1:8082",       # your second node
    "https://your-public-node.com"
]

def sync_to_peers():
    for seed in sim.top(3):
        for peer in PEERS:
            try:
                res = requests.post(f"{peer}/submit", json={"vision": seed.vision})
                print(f"✅ Synced to {peer}: {seed.vision}")
            except Exception as e:
                print(f"❌ Failed to sync to {peer}: {e}")