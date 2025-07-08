from data.finnhub_client import get_news
from alerts.email_notifier import send_email

def scan_news_and_alert():
    headlines = get_news("AAPL")  # or general
    for item in headlines[:5]:
        summary = item.get("headline", "")
        if any(w in summary.lower() for w in ["downgrade", "collapse", "lawsuit", "bankruptcy"]):
            send_email("⚠️ Breaking News Alert", summary)
            break

if __name__ == "__main__":
    scan_news_and_alert()
