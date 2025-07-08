import json
import os
import pandas as pd

PERF_PATH = "memory/performance"
CONFIDENCE_PATH = "memory/confidence_scores.json"

def load_confidences():
    if not os.path.exists(CONFIDENCE_PATH):
        return {}
    return json.load(open(CONFIDENCE_PATH))

def load_recent_pnls(days=5):
    files = sorted(os.listdir(PERF_PATH))[-days:]
    perf_data = []
    for f in files:
        perf_data.append(json.load(open(os.path.join(PERF_PATH, f))))
    return perf_data

def compute_scaling(perf_data, conf_scores):
    score = {}
    for strat in conf_scores:
        pnl_sum = sum(day.get(strat, {}).get("pnl", 0) for day in perf_data)
        conf = conf_scores.get(strat, 0.5)
        scaled = max(0.2, min(1.5, 0.5 + conf + pnl_sum / 1000))
        score[strat] = round(scaled, 3)
    return score

if __name__ == "__main__":
    perf = load_recent_pnls()
    conf = load_confidences()
    result = compute_scaling(perf, conf)
    print("📊 Capital Scaling Weights (by strategy):")
    for k, v in result.items():
        print(f"{k}: ×{v}")
    