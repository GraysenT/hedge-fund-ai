import os
import time
from datetime import datetime
from alerts.slack_notifier import send_slack_alert

def check_health():
    try:
        last_modified = os.path.getmtime("logs/trade_history.json")
        delay = time.time() - last_modified
        if delay > 300:
            send_slack_alert(f"⚠️ No trades in 5+ minutes — check system", tag="UPTIME")
    except Exception as e:
        send_slack_alert(f"❌ Uptime check failed: {e}", tag="UPTIME")

if __name__ == "__main__":
    check_health()