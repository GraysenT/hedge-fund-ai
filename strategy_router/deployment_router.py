import os
import json
from utils.paths import STRATEGY_STATUS_FILE, DEPLOYMENT_STATUS_FILE

def run_deployment_filter(approved_strategies, min_sharpe=0.2):
    deployed = []

    # Load scores
    if os.path.exists(STRATEGY_STATUS_FILE):
        with open(STRATEGY_STATUS_FILE, "r") as f:
            scores = json.load(f)
    else:
        scores = {}

    for strat in approved_strategies:
        strat_score = scores.get(strat, {}).get("sharpe", 0)
        if strat_score >= min_sharpe:
            deployed.append(strat)

    # Save to deployment status
    status = {}
    for strat in deployed:
        status[strat] = {"deployed": True}

    with open(DEPLOYMENT_STATUS_FILE, "w") as f:
        json.dump(status, f, indent=2)

    print(f"[DEPLOYMENT] Final deployed strategies: {deployed}")
    return deployed