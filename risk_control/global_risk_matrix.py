import json
import os
import pandas as pd
import random

TRADES_LOG = "logs/trade_history.json"
RISK_MATRIX = "memory/global_risk_matrix.json"

def generate_risk_matrix():
    if not os.path.exists(TRADES_LOG):
        print("❌ Trade log not found.")
        return

    with open(TRADES_LOG, "r") as f:
        trades = json.load(f)

    df = pd.DataFrame(trades)

    matrix = []
    for strategy in df["strategy"].unique():
        strat_trades = df[df["strategy"] == strategy]
        pnl = strat_trades["pnl"].sum()
        vol = strat_trades["pnl"].std() or 0
        trades_count = len(strat_trades)
        drawdown = pnl * random.uniform(0.2, 0.5)

        red_flag_raw = abs(drawdown) > abs(pnl) * 0.6 or vol > 0.5
        red_flag = bool(red_flag_raw)  # ✅ ensure it's a native Python bool

        matrix.append({
            "strategy": strategy,
            "pnl": round(pnl, 2),
            "volatility": round(vol, 3),
            "drawdown_est": round(drawdown, 2),
            "risk_score": round((abs(drawdown) + vol) / (abs(pnl) + 1e-6), 2),
            "red_flag": red_flag  # ✅ now always serializable
        })

    with open(RISK_MATRIX, "w") as f:
        json.dump(matrix, f, indent=2)

    print(f"🧯 Global risk matrix generated for {len(matrix)} strategies.")

if __name__ == "__main__":
    generate_risk_matrix()