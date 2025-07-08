import os
import json
import pandas as pd
from datetime import datetime

TRADES_LOG = "logs/trade_history.json"
ATTRIBUTION_LOG = "memory/alpha_attribution.json"

def generate_alpha_attribution():
    if not os.path.exists(TRADES_LOG):
        print("❌ No trade log found.")
        return

    with open(TRADES_LOG, "r") as f:
        trades = json.load(f)

    df = pd.DataFrame(trades)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Group by strategy or signal label
    grouped = df.groupby("strategy").agg(
        pnl_total=pd.NamedAgg(column="pnl", aggfunc="sum"),
        trades=pd.NamedAgg(column="pnl", aggfunc="count"),
        avg_return=pd.NamedAgg(column="pnl", aggfunc="mean")
    ).reset_index()

    grouped["timestamp"] = datetime.utcnow().isoformat()
    grouped = grouped.sort_values("pnl_total", ascending=False)

    grouped.to_json(ATTRIBUTION_LOG, orient="records", indent=2)
    print(f"📈 Alpha attribution generated for {len(grouped)} strategies.")

if __name__ == "__main__":
    generate_alpha_attribution()