import json
import os
from datetime import datetime

ATTRIBUTION_LOG = "memory/alpha_attribution.json"
RETIRED_FILE = "memory/retired_strategies.json"
REVIVED_FILE = "memory/revived_strategies.json"

def retire_decay_strategies(threshold_pnl=-500, min_trades=20):
    """
    Retire strategies that have underperformed based on total PnL and minimum trade count.
    """
    if not os.path.exists(ATTRIBUTION_LOG):
        print("⚠️ No attribution data found.")
        return []

    with open(ATTRIBUTION_LOG) as f:
        strategies = json.load(f)

    retired = []
    for s in strategies:
        if s["pnl_total"] < threshold_pnl and s["trades"] >= min_trades:
            retired.append({
                "strategy": s["strategy"],
                "pnl_total": s["pnl_total"],
                "trades": s["trades"],
                "retired_at": datetime.utcnow().isoformat()
            })

    if retired:
        with open(RETIRED_FILE, "w") as f:
            json.dump(retired, f, indent=2)
        print(f"🪦 Retired {len(retired)} decaying strategies.")

    return retired

def check_for_revival(threshold_pnl=100):
    """
    Identify retired strategies that have shown recovery and should be reactivated.
    """
    if not os.path.exists(RETIRED_FILE):
        print("ℹ️ No retired strategies found.")
        return []

    with open(RETIRED_FILE) as f:
        retired = json.load(f)

    revived = []
    for s in retired:
        if s["pnl_total"] > threshold_pnl:
            revived.append({
                "strategy": s["strategy"],
                "recovered_pnl": s["pnl_total"],
                "revived_at": datetime.utcnow().isoformat()
            })

    if revived:
        with open(REVIVED_FILE, "w") as f:
            json.dump(revived, f, indent=2)
        print(f"🔁 Revived {len(revived)} previously retired strategies.")

    return revived

if __name__ == "__main__":
    retire_decay_strategies()
    check_for_revival()