import requests

TELEGRAM_TOKEN = "your_bot_token"
CHAT_ID = "your_chat_id"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": message})