import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ATTRIBUTION_LOG = "memory/alpha_attribution.json"

def show_alpha_dashboard():
    if not os.path.exists(ATTRIBUTION_LOG):
        print("❌ No alpha attribution data.")
        return

    with open(ATTRIBUTION_LOG, "r") as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    df = df.sort_values("pnl_total", ascending=False)

    print("🏆 Top Alpha Contributors:")
    print(df[["strategy", "pnl_total", "avg_return", "trades"]].head(5))

    plt.figure(figsize=(10, 5))
    sns.barplot(x="pnl_total", y="strategy", data=df, palette="viridis")
    plt.title("Total PnL by Strategy")
    plt.xlabel("PnL")
    plt.ylabel("Strategy")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    sns.scatterplot(data=df, x="trades", y="avg_return", hue="strategy", size="pnl_total", palette="coolwarm")
    plt.title("Alpha Source Diagnostics")
    plt.xlabel("# of Trades")
    plt.ylabel("Avg Return")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    show_alpha_dashboard()