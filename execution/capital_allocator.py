import json
import os
from datetime import datetime

BASE_CAPITAL = 1_000_000  # Simulated capital pool

def load_latest_allocations():
    alloc_dir = "memory/scaled_allocations"
    if not os.path.exists(alloc_dir):
        print("❌ No capital allocation folder found.")
        return {}
    latest_file = sorted(os.listdir(alloc_dir))[-1]
    with open(os.path.join(alloc_dir, latest_file), "r") as f:
        return json.load(f), latest_file

def simulate_trade_allocation(scaled_allocs):
    trades = {}
    total_weight = sum(scaled_allocs.values())

    if total_weight == 0:
        print("⚠️ Total capital weight is 0 — no trades made.")
        return trades

    for strat, weight in scaled_allocs.items():
        share = weight / total_weight
        capital = round(BASE_CAPITAL * share, 2)
        trades[strat] = {
            "capital_allocated": capital,
            "weight": weight,
            "share_of_pool": round(share, 4)
        }
        print(f"💼 {strat} → ${capital} (Weight: {weight}, Share: {round(share*100, 2)}%)")

    return trades

def save_executions(trades):
    date_str = datetime.now().strftime("%Y-%m-%d")
    folder = "memory/executions"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{date_str}.json")

    with open(path, "w") as f:
        json.dump(trades, f, indent=2)
    print(f"\n✅ Saved simulated executions to {path}")

if __name__ == "__main__":
    scaled_allocs, alloc_file = load_latest_allocations()
    print(f"\n📥 Loaded capital weights from: {alloc_file}")

    trades = simulate_trade_allocation(scaled_allocs)
    save_executions(trades)