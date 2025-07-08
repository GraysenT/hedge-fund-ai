import pandas as pd
import requests
from pathlib import Path
from datetime import datetime

FUND_LOG = Path("audit/fund_balance.csv")
ALERT_LOG = Path("memory/last_alert.txt")
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/your_webhook_here"
DRAW_THRESHOLD = 0.05  # 5% drop from recent high

def send_discord_alert(message):
    payload = {"content": f"🚨 {message}"}
    try:
        requests.post(DISCORD_WEBHOOK, json=payload)
        print("✅ Alert sent to Discord.")
    except Exception as e:
        print(f"❌ Discord alert failed: {e}")

def check_drawdown():
    if not FUND_LOG.exists():
        return

    df = pd.read_csv(FUND_LOG)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")
    balances = df["balance"]

    peak = balances.max()
    latest = balances.iloc[-1]
    drawdown = (peak - latest) / peak

    if drawdown >= DRAW_THRESHOLD:
        last_alert = ""
        if ALERT_LOG.exists():
            last_alert = ALERT_LOG.read_text().strip()
        if last_alert != df["date"].iloc[-1].strftime("%Y-%m-%d"):
            msg = f"Fund drawdown alert! Current: ${latest:,.2f}, Peak: ${peak:,.2f}, DD: {drawdown:.2%}"
            send_discord_alert(msg)
            ALERT_LOG.write_text(df["date"].iloc[-1].strftime("%Y-%m-%d"))