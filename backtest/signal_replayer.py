import json
import os
import pandas as pd

SIGNAL_PATH = "memory/signal_history.json"
PRICE_PATH = "data/price_history/"
RESULT_PATH = "backtest/results"

os.makedirs(RESULT_PATH, exist_ok=True)

def load_signals():
    with open(SIGNAL_PATH, "r") as f:
        return json.load(f)

def load_price(symbol):
    path = os.path.join(PRICE_PATH, f"{symbol}.csv")
    if not os.path.exists(path):
        return pd.DataFrame()
    return pd.read_csv(path, parse_dates=["timestamp"])

def simulate_return(entry_price, exit_price, direction):
    change = (exit_price - entry_price) / entry_price
    return round(change if direction == "buy" else -change, 4)

def replay_signals(signals):
    results = {}
    for strat, events in signals.items():
        total_pnl = 0
        count = 0
        for sig in events:
            symbol = sig["symbol"]
            ts = sig["timestamp"]
            direction = sig["action"]
            df = load_price(symbol)
            if df.empty:
                continue
            row = df[df["timestamp"] == ts]
            if row.empty:
                continue
            entry = float(row["close"].iloc[0])
            next_row = df[df["timestamp"] > ts].head(1)
            if next_row.empty:
                continue
            exit = float(next_row["close"].iloc[0])
            ret = simulate_return(entry, exit, direction)
            total_pnl += ret
            count += 1
        results[strat] = {
            "Signals Replayed": count,
            "Total Return": round(total_pnl, 4),
            "Avg Return": round(total_pnl / count, 4) if count > 0 else 0
        }

    with open(os.path.join(RESULT_PATH, "replay_summary.json"), "w") as f:
        json.dump(results, f, indent=2)

    print("✅ Signal replay complete:")
    for s, r in results.items():
        print(f"{s}: {r}")

if __name__ == "__main__":
    signals = load_signals()
    replay_signals(signals)
