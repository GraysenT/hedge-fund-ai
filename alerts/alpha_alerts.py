import pandas as pd
from pathlib import Path
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

ALPHA_STATUS = Path("memory/alpha_defense_status.csv")
EMAIL_TO = "graysentorczon@icloud.com"
FROM_EMAIL = "your_email@example.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_PASS = "your_app_password"

def send_alpha_alert(muted_strategies):
    subject = f"🚨 Alpha Breakdown Detected [{datetime.utcnow().strftime('%Y-%m-%d')}]"
    body = f"The following strategies were muted due to alpha decay:\n\n" + "\n".join(muted_strategies)

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = FROM_EMAIL
    msg["To"] = EMAIL_TO

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(FROM_EMAIL, EMAIL_PASS)
            server.sendmail(FROM_EMAIL, [EMAIL_TO], msg.as_string())
        print("✅ Alpha alert sent via email.")
    except Exception as e:
        print("❌ Failed to send alert:", e)

def run_alpha_alert():
    if ALPHA_STATUS.exists():
        df = pd.read_csv(ALPHA_STATUS)
        muted = df[df["status"] == "muted"]["strategy"].tolist()
        if muted:
            send_alpha_alert(muted)