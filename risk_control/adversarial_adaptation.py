import json
import os
from datetime import datetime

ALPHA_LOG = "memory/alpha_attribution.json"
ADAPT_LOG = "logs/adversarial_adaptation.log"

def adapt_to_adversity(pnl_threshold=-300, signal_drop_rate=0.5):
    if not os.path.exists(ALPHA_LOG):
        print("❌ No alpha attribution file.")
        return

    with open(ALPHA_LOG, "r") as f:
        strategies = json.load(f)

    flagged = []
    for strat in strategies:
        pnl = strat.get("pnl_total", 0)
        trades = strat.get("trades", 0)
        avg_return = strat.get("avg_return", 0)

        if trades > 10 and pnl < pnl_threshold and avg_return < 0:
            flagged.append({
                "strategy": strat["strategy"],
                "pnl": pnl,
                "avg_return": avg_return,
                "timestamp": datetime.utcnow().isoformat(),
                "action": "reduce_weight",
                "reason": "Adversarial pattern detected"
            })

    if flagged:
        os.makedirs("logs", exist_ok=True)
        with open(ADAPT_LOG, "a") as f:
            for entry in flagged:
                f.write(json.dumps(entry) + "\n")
        print(f"🛡️ Adversarial adaptation triggered for {len(flagged)} strategies.")
    else:
        print("✅ No adversarial adaptation needed.")

if __name__ == "__main__":
    adapt_to_adversity()