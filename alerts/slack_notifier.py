import json
import os
import requests

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK_URL", "https://hooks.slack.com/services/...")
ALERT_LOG = "logs/alerts.log"

def send_slack_alert(message, tag="INFO"):
    if "hooks.slack.com" not in SLACK_WEBHOOK:
        print("⚠️ Slack webhook not set.")
        return

    payload = {
        "text": f"[{tag}] {message}"
    }
    try:
        requests.post(SLACK_WEBHOOK, json=payload)
        with open(ALERT_LOG, "a") as f:
            f.write(f"[{tag}] {message}\n")
        print(f"📤 Slack alert sent: {message}")
    except Exception as e:
        print(f"❌ Failed to send Slack alert: {e}")

if __name__ == "__main__":
    send_slack_alert("🚀 System online and all modules validated", tag="BOOT")