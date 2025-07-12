import os
import json
from utils.paths import STRATEGY_STATUS_FILE

def get_underperformers(min_sharpe=-10.0, max_sharpe=0.2, max_results=10):
    """
    Returns a list of underperforming strategy names based on Sharpe ratio.
    Pulls from STRATEGY_STATUS_FILE if it exists; otherwise falls back to default list.
    """
    underperformers = []

    if os.path.exists(STRATEGY_STATUS_FILE):
        try:
            with open(STRATEGY_STATUS_FILE, "r") as f:
                data = json.load(f)

            for strategy, stats in data.items():
                sharpe = stats.get("sharpe", 0.0)
                if min_sharpe <= sharpe <= max_sharpe:
                    underperformers.append(strategy)
                if len(underperformers) >= max_results:
                    break

        except Exception as e:
            print(f"⚠️ simulation_memory: Error loading strategy stats — {e}")

    # Fallback list if nothing found
    if not underperformers:
        underperformers = [
            "mean_reversion_noise",
            "macro_blindspot",
            "volume_gap_hunter",
            "fake_breakout_lagger",
            "slow_react_scalper"
        ][:max_results]

    return underperformers