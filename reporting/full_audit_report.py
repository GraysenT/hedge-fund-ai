import json
import os
from datetime import datetime

def generate_audit():
    lines = ["📋 Full-System Audit Snapshot"]
    lines.append(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("-" * 40)

    # Capital
    alloc = json.load(open("memory/scaled_allocations/" + sorted(os.listdir("memory/scaled_allocations"))[-1]))
    lines.append("💸 Capital Allocations:")
    for k, v in alloc.items():
        lines.append(f" - {k}: {round(v*1_000_000, 2)}")

    # Performance
    perf = json.load(open("memory/performance/" + sorted(os.listdir("memory/performance"))[-1]))
    lines.append("\n📈 Strategy PnL:")
    for k, v in perf.items():
        lines.append(f" - {k}: ${round(v['pnl'],2)}")

    # Firewall
    if os.path.exists("meta/alpha_firewall.json"):
        blocked = json.load(open("meta/alpha_firewall.json"))
        lines.append(f"\n🚫 Firewalled Strategies: {', '.join(blocked)}")

    path = f"reporting/audits/audit_{datetime.now().strftime('%Y-%m-%d')}.txt"
    os.makedirs("reporting/audits", exist_ok=True)
    with open(path, "w") as f:
        f.write("\n".join(lines))

    print(f"✅ Audit saved to {path}")

if __name__ == "__main__":
    generate_audit()
    