import os
import json
from collections import defaultdict
import pandas as pd

LOG_DIR = "strategy_memory/evolution_logs"

# Thresholds
PROMOTION_THRESHOLD = 2
MUTE_THRESHOLD = 2


def load_evolution_logs():
    logs = []
    files = sorted([f for f in os.listdir(LOG_DIR) if f.endswith(".json")])
    for f_name in files:
        with open(os.path.join(LOG_DIR, f_name), 'r') as f:
            log = json.load(f)
            log_ts = log.get("timestamp")
            for strat in log.get("muted_strategies", []):
                logs.append((log_ts, strat, "muted"))
            for strat in log.get("promoted_strategies", []):
                logs.append((log_ts, strat, "promoted"))
    return logs


def analyze_strategy_health(logs):
    health = defaultdict(lambda: {"promoted": 0, "muted": 0})
    for _, strat, action in logs:
        health[strat][action] += 1

    results = []
    for strat, counts in health.items():
        p, m = counts["promoted"], counts["muted"]
        if m >= MUTE_THRESHOLD:
            rating = "🔴 Retire"
        elif p >= PROMOTION_THRESHOLD:
            rating = "🟢 Strong"
        else:
            rating = "🟡 Watch"

        results.append({
            "Strategy": strat,
            "Promoted": p,
            "Muted": m,
            "Oversight Rating": rating
        })

    return pd.DataFrame(results)


if __name__ == '__main__':
    log_entries = load_evolution_logs()
    df = analyze_strategy_health(log_entries)
    print("\n📊 AI Oversight Ratings:")
    print(df.sort_values(by=["Oversight Rating", "Promoted"], ascending=[True, False]).to_string(index=False))
    