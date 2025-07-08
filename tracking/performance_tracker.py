import json
import os
from datetime import datetime
import random

EXEC_PATH = "memory/executions"
PERF_PATH = "memory/performance"

def load_latest_executions():
    if not os.path.exists(EXEC_PATH):
        print("❌ No executions folder found.")
        return {}, "none"
    files = sorted(os.listdir(EXEC_PATH))
    if not files:
        print("⚠️ No executions found.")
        return {}, "none"
    latest_file = files[-1]
    with open(os.path.join(EXEC_PATH, latest_file), "r") as f:
        return json.load(f), latest_file

def simulate_strategy_pnl(trades):
    performance = {}
    for strat, trade in trades.items():
        capital = trade["capital_allocated"]

        # Simulate return between -5% to +5%
        ret_pct = round(random.uniform(-0.05, 0.05), 4)
        pnl = round(capital * ret_pct, 2)

        performance[strat] = {
            "capital_allocated": capital,
            "return_pct": ret_pct,
            "pnl": pnl
        }

        arrow = "📈" if pnl > 0 else "📉"
        print(f"{arrow} {strat} → PnL: ${pnl} ({ret_pct * 100}%)")

    return performance

def save_performance(performance):
    os.makedirs(PERF_PATH, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    path = os.path.join(PERF_PATH, f"{date_str}.json")
    with open(path, "w") as f:
        json.dump(performance, f, indent=2)
    print(f"\n✅ Saved daily performance to {path}")

if __name__ == "__main__":
    trades, source_file = load_latest_executions()
    print(f"\n📊 Tracking performance for: {source_file}")
    if trades:
        results = simulate_strategy_pnl(trades)
        save_performance(results)
