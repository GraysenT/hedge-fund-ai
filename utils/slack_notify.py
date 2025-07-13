import requests

def notify_slack(message: str):
    webhook = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
    payload = {"text": message}
    response = requests.post(webhook, json=payload)
    return response.status_code == 200
