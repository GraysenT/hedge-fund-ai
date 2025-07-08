import json
import os
import requests
from datetime import datetime

def export_strategies():
    lineage = json.load(open("strategy_memory/strategy_lineage.json"))
    perf_file = sorted(os.listdir("memory/performance"))[-1]
    perf = json.load(open(f"memory/performance/{perf_file}"))

    export = {
        "date": datetime.now().isoformat(),
        "strategies": lineage,
        "performance": perf
    }

    with open("federation/export_bundle.json", "w") as f:
        json.dump(export, f, indent=2)
    print("📦 Export bundle created.")

def push_to_peer(url):
    bundle = json.load(open("federation/export_bundle.json"))
    r = requests.post(url, json=bundle)
    print(f"➡️ Sent bundle to peer: {r.status_code}")

if __name__ == "__main__":
    export_strategies()
    # push_to_peer("http://peer-node:8000/federation/receive")
    