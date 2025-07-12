"""
Disables a strategy when recent performance drops sharply.
Can be plugged into the capital allocator or execution veto layer.
"""

from utils.paths import STRATEGY_STATUS_FILE
import json
import os

def is_strategy_broken(strategy_name, min_sharpe=-1.0, max_drawdown=0.15):
    """
    Returns True if strategy should be killed based on recent performance.
    """
    if not os.path.exists(STRATEGY_STATUS_FILE):
        return False

    try:
        with open(STRATEGY_STATUS_FILE, "r") as f:
            data = json.load(f)

        stats = data.get(strategy_name, {})
        sharpe = stats.get("sharpe", 0.0)
        drawdown = stats.get("max_drawdown", 0.0)

        return sharpe < min_sharpe or drawdown > max_drawdown

    except Exception as e:
        print(f"[Killswitch] Error: {e}")
        return False