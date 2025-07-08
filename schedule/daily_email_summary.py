from alerts.email_notifier import send_email
import json
import os

def send_summary():
    subject = "📊 Daily Strategy Summary"
    lines = []

    try:
        with open("strategy_memory/deployment_status.json") as f:
            deploy = json.load(f)
        approved = [k for k, v in deploy.items() if v.get("approved")]
        lines.append(f"✅ Approved Strategies: {', '.join(approved)}")
    except:
        pass

    try:
        latest_alloc = sorted(os.listdir("memory/scaled_allocations"))[-1]
        with open(os.path.join("memory/scaled_allocations", latest_alloc)) as f:
            allocs = json.load(f)
        lines.append(f"\n💸 Capital Allocations:")
        for k, v in allocs.items():
            lines.append(f"  - {k}: ${round(v * 1_000_000, 2)}")
    except:
        pass

    try:
        latest_pnl = sorted(os.listdir("memory/performance"))[-1]
        with open(os.path.join("memory/performance", latest_pnl)) as f:
            pnl = json.load(f)
        lines.append(f"\n📈 PnL:")
        for k, v in pnl.items():
            lines.append(f"  - {k}: {round(v['pnl'], 2)} ({round(v['return_pct'] * 100, 2)}%)")
    except:
        pass

    send_email(subject, "\n".join(lines))

if __name__ == "__main__":
    send_summary()
    