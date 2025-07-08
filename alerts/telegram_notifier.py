import os
import requests

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_alert(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("⚠️ Telegram credentials not set.")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, data=payload)
        if response.ok:
            print(f"📲 Telegram alert sent: {message}")
        else:
            print(f"❌ Failed: {response.text}")
    except Exception as e:
        print(f"❌ Telegram alert error: {e}")

if __name__ == "__main__":
    send_telegram_alert("🚀 Hedge Fund AI is now running live.")