import schedule
import time
from datetime import datetime
from reports.daily_email_report import send_email

# Time to send the email (8:30 AM Central Time assumed)
SEND_HOUR = 8
SEND_MINUTE = 30


def job():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n🕗 [{now}] Running daily alpha email job...")
    try:
        send_email()
    except Exception as e:
        print(f"❌ Error sending daily alpha email: {e}")


# Schedule the job every day at 8:30 AM
schedule.every().day.at("08:30").do(job)

print("📅 Email scheduler initialized. Waiting for 8:30 AM...")

while True:
    schedule.run_pending()
    time.sleep(30)
