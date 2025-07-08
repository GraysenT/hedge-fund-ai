import json
import random
from datetime import datetime

CLIENTS = {
    "clientA": {"risk": "high", "objective": "growth"},
    "clientB": {"risk": "low", "objective": "income"}
}

STRATEGIES = {
    "strat_fast": {"vol": 0.03, "alpha": 0.12},
    "strat_defensive": {"vol": 0.01, "alpha": 0.04}
}

def allocate():
    allocation = {}
    for client, prefs in CLIENTS.items():
        allocation[client] = {}
        for strat, stats in STRATEGIES.items():
            if prefs["risk"] == "low" and stats["vol"] <= 0.015:
                allocation[client][strat] = 0.7
            elif prefs["risk"] == "high":
                allocation[client][strat] = 0.5
    path = f"memory/client_allocations/{datetime.now().strftime('%Y-%m-%d')}.json"
    with open(path, "w") as f:
        json.dump(allocation, f, indent=2)
    print(f"📊 Multi-client allocation written to {path}")

if __name__ == "__main__":
    allocate()
