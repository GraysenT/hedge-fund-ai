import json
import os
from datetime import datetime

LINEAGE = "strategy_memory/strategy_lineage.json"
MISSION_LOG = "meta/mission_status.json"

MISSION = {
    "target_style": "momentum",
    "max_depth": 7,
    "allowed_models": ["LSTM", "Transformer"]
}

def check_alignment():
    lineage = json.load(open(LINEAGE))
    log = {"drift": [], "timestamp": datetime.now().isoformat()}

    for strat, meta in lineage.items():
        depth = meta.get("depth", 0)
        model = meta.get("model", "")
        rating = meta.get("rating", "")

        if depth > MISSION["max_depth"]:
            log["drift"].append(f"{strat} exceeds depth limit: {depth}")
        if model not in MISSION["allowed_models"]:
            log["drift"].append(f"{strat} uses model outside policy: {model}")
        if "contrarian" in rating.lower() and "momentum" in MISSION["target_style"]:
            log["drift"].append(f"{strat} marked contrarian, violates style")

    with open(MISSION_LOG, "w") as f:
        json.dump(log, f, indent=2)

    print("🛡 Mission status logged.")
    for d in log["drift"]:
        print(f"⚠️  {d}")

if __name__ == "__main__":
    check_alignment()
    