import os
import json
from utils.paths import MUTED_STRATEGIES_FILE, REWARDED_STRATEGIES_FILE

# Ensure the files exist
def _ensure_file(path):
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump([], f)

# Load list of muted strategies
def load_muted_strategies():
    _ensure_file(MUTED_STRATEGIES_FILE)
    try:
        with open(MUTED_STRATEGIES_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"[TRIGGERS] Failed to load muted strategies: {e}")
        return []

# Load list of rewarded strategies
def load_rewarded_strategies():
    _ensure_file(REWARDED_STRATEGIES_FILE)
    try:
        with open(REWARDED_STRATEGIES_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"[TRIGGERS] Failed to load rewarded strategies: {e}")
        return []

# Add a strategy to the muted list
def mute_strategy(strategy_name):
    muted = load_muted_strategies()
    if strategy_name not in muted:
        muted.append(strategy_name)
        with open(MUTED_STRATEGIES_FILE, "w") as f:
            json.dump(muted, f, indent=2)
        print(f"[TRIGGERS] Strategy muted: {strategy_name}")

# Add a strategy to the rewarded list
def reward_strategy(strategy_name):
    rewarded = load_rewarded_strategies()
    if strategy_name not in rewarded:
        rewarded.append(strategy_name)
        with open(REWARDED_STRATEGIES_FILE, "w") as f:
            json.dump(rewarded, f, indent=2)
        print(f"[TRIGGERS] Strategy rewarded: {strategy_name}")