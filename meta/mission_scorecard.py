import json
import os

LINEAGE = "strategy_memory/strategy_lineage.json"
PERF_PATH = "memory/performance"

MISSION = {
    "target_style": "momentum",
    "approved_models": ["LSTM", "Transformer"]
}

def score_mission():
    lineage = json.load(open(LINEAGE))
    perf = json.load(open(f"{PERF_PATH}/{sorted(os.listdir(PERF_PATH))[-1]}"))

    active = [s for s in perf if perf[s]["pnl"] > 0]
    aligned_models = sum(1 for s in active if lineage[s].get("model") in MISSION["approved_models"])
    total = len(active)

    score = round(100 * aligned_models / total, 2) if total else 0
    print(f"🎯 Mission Alignment Score: {score}%")
    print(f"Aligned Models: {aligned_models}/{total}")

if __name__ == "__main__":
    score_mission()
    