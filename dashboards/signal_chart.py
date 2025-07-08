import pandas as pd
import matplotlib.pyplot as plt
import json

price = pd.read_csv("data/price_history/TSLA.csv")
with open("memory/signal_history.json") as f:
    signals = json.load(f)

tsla_signals = [s for s in signals.get("gen_strat_r2", []) if s["symbol"] == "TSLA"]

plt.figure(figsize=(14, 6))
plt.plot(price["timestamp"], price["close"], label="TSLA Price")

for s in tsla_signals:
    idx = price[price["timestamp"] == s["timestamp"]].index
    if not idx.empty:
        color = "green" if s["action"] == "buy" else "red"
        plt.scatter(s["timestamp"], price.loc[idx[0], "close"], color=color, label=s["action"], alpha=0.7)

plt.title("TSLA Price + Signal Overlay")
plt.xlabel("Time")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
