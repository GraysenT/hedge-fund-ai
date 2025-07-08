import json
import os

PERF_PATH = "memory/performance"
LINEAGE_PATH = "strategy_memory/strategy_lineage.json"

def diagnose_and_repair(threshold=-50):
    file = sorted(os.listdir(PERF_PATH))[-1]
    perf = json.load(open(f"{PERF_PATH}/{file}"))
    lineage = json.load(open(LINEAGE_PATH))

    for strat, res in perf.items():
        pnl = res["pnl"]
        rating = lineage.get(strat, {}).get("rating", "")
        if pnl < threshold or "Poor" in rating:
            action = "mutate" if "mut" not in strat else "kill"
            print(f"🩺 {strat} flagged → Action: {action.upper()}")
            # Write flag to mutation queue
            with open("meta/repair_queue.txt", "a") as f:
                f.write(f"{strat}:{action}\n")

if __name__ == "__main__":
    diagnose_and_repair()
    