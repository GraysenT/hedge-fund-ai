import json
import os
import pandas as pd

strategy = input("🔍 Enter strategy ID to inspect: ")

# Load all relevant files
with open("strategy_memory/deployment_status.json") as f:
    deploy = json.load(f)

with open("memory/strategy_lineage.json") as f:
    lineage = json.load(f)

try:
    with open("backtest/results/replay_summary.json") as f:
        replay = json.load(f)
except:
    replay = {}

# Load cumulative PnL
from tracking.cumulative_tracker import PERF_PATH
cumulative = {}
for file in sorted(os.listdir(PERF_PATH)):
    with open(os.path.join(PERF_PATH, file)) as f:
        daily = json.load(f)
        if strategy in daily:
            if strategy not in cumulative:
                cumulative[strategy] = {
                    "Total PnL": 0,
                    "Days": 0
                }
            cumulative[strategy]["Total PnL"] += daily[strategy]["pnl"]
            cumulative[strategy]["Days"] += 1

# Display Report
print(f"\n📋 Strategy Report: {strategy}\n")

if strategy in lineage:
    info = lineage[strategy]
    print(f"Depth: {info['depth']}  |  Sharpe: {info['sharpe']}  |  Rating: {info['rating']}")

if strategy in deploy:
    status = "✅ Approved" if deploy[strategy]["approved"] else "❌ Rejected"
    print(f"Deployment Status: {status}  |  Net Votes: {deploy[strategy]['net']}")

if strategy in cumulative:
    stats = cumulative[strategy]
    print(f"Total PnL: ${round(stats['Total PnL'],2)}  |  Days Traded: {stats['Days']}")

if strategy in replay:
    r = replay[strategy]
    print(f"Replay Accuracy: {r['Total Return']} total | {r['Avg Return']} avg")

print("\n✅ Strategy inspection complete.")
