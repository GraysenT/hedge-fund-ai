import json
import os
import pandas as pd
import matplotlib.pyplot as plt

TRADES_LOG = "logs/trade_history.json"

def show_longevity_dashboard():
    if not os.path.exists(TRADES_LOG):
        return

    df = pd.read_json(TRADES_LOG)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["day"] = df["timestamp"].dt.date

    lifetime = df.groupby("strategy")["day"].nunique().sort_values(ascending=False)
    pnl = df.groupby("strategy")["pnl"].sum()

    print("📈 Strategy Longevity Leaderboard:")
    print(lifetime.head(5))

    plt.figure(figsize=(10, 5))
    plt.bar(lifetime.index[:10], lifetime.values[:10], color="green")
    plt.xticks(rotation=45)
    plt.title("Top 10 Longest-Lived Strategies")
    plt.ylabel("Days Active")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    show_longevity_dashboard()