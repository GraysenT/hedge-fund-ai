import json
import os
from datetime import datetime

def generate_summary():
    lines = ["📊 Daily Hedge Fund AI Summary", "-"*40]

    latest_alloc = sorted(os.listdir("memory/scaled_allocations"))[-1]
    allocs = json.load(open(f"memory/scaled_allocations/{latest_alloc}"))
    lines.append("💸 Capital Allocation:")
    for k, v in allocs.items():
        lines.append(f" - {k}: ${round(v*1_000_000, 2)}")

    perf = sorted(os.listdir("memory/performance"))[-1]
    pnl = json.load(open(f"memory/performance/{perf}"))
    lines.append("\n📈 Performance:")
    for k, v in pnl.items():
        lines.append(f" - {k}: {round(v['pnl'], 2)} ({round(v['return_pct']*100, 2)}%)")

    plugins = json.load(open("plugins/plugin_log.json"))
    lines.append("\n📦 Plugins Run:")
    for k, v in plugins.items():
        lines.append(f" - {k}: {v.get('result', 'No output')}")

    report = "\n".join(lines)
    with open("reporting/daily_report.txt", "w") as f:
        f.write(report)
    print("✅ Report generated at reporting/daily_report.txt")

if __name__ == "__main__":
    generate_summary()
