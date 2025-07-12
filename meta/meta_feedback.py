import os
import json
from utils.paths import TRADE_LOG_FILE, STRATEGY_STATUS_FILE

def update_strategy_scores():
    if not os.path.exists(TRADE_LOG_FILE):
        print("[META] No trade log found.")
        return

    try:
        with open(TRADE_LOG_FILE, "r") as f:
            trade_log = json.load(f)
    except Exception as e:
        print(f"[META] Failed to read trade log: {e}")
        return

    stats = {}

    for entry in trade_log:
        executions = entry.get("executions", {})
        for strat, result in executions.items():
            if not isinstance(result, dict):
                continue
            pnl = result.get("pnl", 0)
            status = result.get("status", "")
            if status != "executed":
                continue

            if strat not in stats:
                stats[strat] = {"returns": [], "win": 0, "loss": 0}

            stats[strat]["returns"].append(pnl)
            if pnl > 0:
                stats[strat]["win"] += 1
            elif pnl < 0:
                stats[strat]["loss"] += 1

    # Compute Sharpe-like score
    final_scores = {}
    for strat, data in stats.items():
        rets = data["returns"]
        if not rets:
            continue
        avg = sum(rets) / len(rets)
        vol = (sum((r - avg)**2 for r in rets) / len(rets)) ** 0.5
        sharpe = avg / vol if vol > 0 else 0
        win_rate = data["win"] / max(data["win"] + data["loss"], 1)
        final_scores[strat] = {
            "sharpe": round(sharpe, 3),
            "win_rate": round(win_rate, 3),
            "trades": len(rets)
        }

    with open(STRATEGY_STATUS_FILE, "w") as f:
        json.dump(final_scores, f, indent=2)

    print("[META] Updated strategy scores.")