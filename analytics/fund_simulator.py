import json
import os
import pandas as pd

TRADES_LOG = "logs/trade_history.json"

def simulate_fund_lifetime():
    if not os.path.exists(TRADES_LOG):
        return

    with open(TRADES_LOG) as f:
        trades = pd.DataFrame(json.load(f))

    trades["timestamp"] = pd.to_datetime(trades["timestamp"])
    trades["day"] = trades["timestamp"].dt.date

    df = trades.groupby(["strategy", "day"]).agg(
        pnl=("pnl", "sum"),
        trades=("pnl", "count")
    ).reset_index()

    print("📆 Strategy Lifespan Summary:")
    for strat in df["strategy"].unique():
        strat_df = df[df["strategy"] == strat]
        days_active = strat_df["day"].nunique()
        total_pnl = strat_df["pnl"].sum()
        print(f" - {strat}: {days_active} days active | PnL: {round(total_pnl,2)}")

if __name__ == "__main__":
    simulate_fund_lifetime()