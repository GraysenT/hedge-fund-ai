import json
import os

TRUST_FILE = "federation/trust_network.json"
ALLOCATIONS = "federation/capital_allocations.json"

def allocate():
    if not os.path.exists(TRUST_FILE):
        print("❌ No trust data found.")
        return

    trust = json.load(open(TRUST_FILE))
    total_cap = 1_000_000
    total_score = sum(trust.values())

    alloc = {node: round((score / total_score) * total_cap, 2) for node, score in trust.items()}
    json.dump(alloc, open(ALLOCATIONS, "w"), indent=2)
    print("💰 Capital allocated across federation:")
    for node, amt in alloc.items():
        print(f"{node}: ${amt}")

if __name__ == "__main__":
    allocate()
    