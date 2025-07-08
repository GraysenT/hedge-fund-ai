import os
import json
from alerts.slack_notifier import send_slack_alert
from alerts.telegram_notifier import send_telegram_alert

SIGNAL_LOG = "logs/signal_events.json"

def alert_signal_events():
    if not os.path.exists(SIGNAL_LOG):
        return

    with open(SIGNAL_LOG) as f:
        signals = json.load(f)

    for signal in signals[-5:]:
        msg = f"📡 {signal['strategy']} → {signal['action']} {signal['asset']} (conf: {signal['confidence']})"
        send_slack_alert(msg, tag="SIGNAL")
        send_telegram_alert(msg)