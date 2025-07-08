import json
import os
from datetime import datetime, timedelta

PERF_PATH = "memory/performance"
MUTE_FILE = "strategy_memory/self_veto.json"

def update_self_veto():
    veto = json.load(open(MUTE_FILE)) if os.path.exists(MUTE_FILE) else {}

    file = sorted(os.listdir(PERF_PATH))[-1]
    day = json.load(open(f"{PERF_PATH}/{file}"))

    for strat, res in day.items():
        if res["pnl"] < -50 or res["return_pct"] < -0.05:
            veto[strat] = (datetime.now() + timedelta(days=2)).isoformat()

    with open(MUTE_FILE, "w") as f:
        json.dump(veto, f, indent=2)

    print(f"🚫 Updated self-veto list for underperformers.")

def is_muted(strat):
    if not os.path.exists(MUTE_FILE):
        return False
    veto = json.load(open(MUTE_FILE))
    if strat not in veto:
        return False
    return datetime.fromisoformat(veto[strat]) > datetime.now()
    