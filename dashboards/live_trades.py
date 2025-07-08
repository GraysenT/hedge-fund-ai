import pandas as pd
import matplotlib.pyplot as plt
import json

def show_live_trades():
    df = pd.read_json("logs/trade_history.json")
    print(df.tail(5))

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df.set_index("timestamp").resample("1H").sum()["pnl"].plot(title="PnL Over Time")
    plt.show()

if __name__ == "__main__":
    show_live_trades()