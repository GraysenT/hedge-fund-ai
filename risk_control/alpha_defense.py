import json
import os
from datetime import datetime

ALPHA_LOG = "memory/alpha_attribution.json"
DEFENSE_LOG = "logs/alpha_defense.log"

def check_alpha_integrity(pnl_threshold=-200, max_drawdown=0.3):
    if not os.path.exists(ALPHA_LOG):
        print("❌ No alpha attribution file.")
        return

    with open(ALPHA_LOG, "r") as f:
        strategies = json.load(f)

    flagged = []
    for strat in strategies:
        pnl = strat.get("pnl_total", 0)
        if pnl < pnl_threshold:
            flagged.append({
                "strategy": strat["strategy"],
                "pnl": pnl,
                "flagged_at": datetime.utcnow().isoformat(),
                "reason": "Low PnL"
            })

    if flagged:
        os.makedirs("logs", exist_ok=True)
        with open(DEFENSE_LOG, "a") as f:
            for entry in flagged:
                f.write(json.dumps(entry) + "\n")
        print(f"🛡️ Alpha defense triggered for {len(flagged)} strategies.")
    else:
        print("🧠 Alpha integrity check passed.")

if __name__ == "__main__":
    check_alpha_integrity()