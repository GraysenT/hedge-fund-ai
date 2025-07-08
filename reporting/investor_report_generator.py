import json
import os
import pandas as pd
from datetime import datetime
from alerts.slack_notifier import send_slack_alert

def generate_investor_report():
    ATTRIBUTION_LOG = "memory/alpha_attribution.json"
    ALLOC_LOG = "memory/optimized_allocations.json"
    TRADE_LOG = "logs/trade_history.json"

    if not all(os.path.exists(p) for p in [ATTRIBUTION_LOG, ALLOC_LOG, TRADE_LOG]):
        print("❌ Missing files for report.")
        return

    with open(ATTRIBUTION_LOG, "r") as f:
        alpha = pd.DataFrame(json.load(f))

    with open(ALLOC_LOG, "r") as f:
        alloc = pd.DataFrame(json.load(f))

    with open(TRADE_LOG, "r") as f:
        trades = pd.DataFrame(json.load(f))

    summary = {
        "Total PnL": round(trades["pnl"].sum(), 2),
        "Avg Daily Return": round(trades["pnl"].mean(), 4),
        "Max Drawdown (est)": round(trades["pnl"].sum() * -0.3, 2),
        "Total Trades": len(trades),
        "Active Strategies": len(alloc)
    }

    report = {
        "timestamp": datetime.utcnow().isoformat(),
        "summary": summary,
        "top_strategies": alpha.sort_values("pnl_total", ascending=False).head(5).to_dict(orient="records"),
        "allocation": alloc.sort_values("weight", ascending=False).to_dict(orient="records") if "weight" in alloc.columns else []
    }

    os.makedirs("reports", exist_ok=True)
    with open("reports/investor_report.json", "w") as f:
        json.dump(report, f, indent=2)

    print(f"🧾 Investor report generated with {summary['Active Strategies']} strategies.")

    # ✅ Send Slack alert after successful generation
    try:
        send_slack_alert(f"📈 Daily report generated — PnL: {summary['Total PnL']}", tag="REPORT")
    except Exception as e:
        print(f"⚠️ Slack alert failed: {e}")

    return report

if __name__ == "__main__":
    generate_investor_report()