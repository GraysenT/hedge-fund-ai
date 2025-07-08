import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from pathlib import Path
from datetime import datetime

EMAIL_TO = "graysentorczon@icloud.com"
FROM_EMAIL = "your_email@example.com"
EMAIL_PASS = "your_app_password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def send_latest_report():
    report_dir = Path("reports/generated")
    latest_pdf = sorted(report_dir.glob("*.pdf"), reverse=True)[0]

    msg = MIMEMultipart()
    msg["Subject"] = f"📄 Weekly Hedge Fund Report ({datetime.utcnow().strftime('%Y-%m-%d')})"
    msg["From"] = FROM_EMAIL
    msg["To"] = EMAIL_TO

    with open(latest_pdf, "rb") as f:
        attachment = MIMEApplication(f.read(), _subtype="pdf")
        attachment.add_header("Content-Disposition", "attachment", filename=latest_pdf.name)
        msg.attach(attachment)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(FROM_EMAIL, EMAIL_PASS)
            server.sendmail(FROM_EMAIL, EMAIL_TO, msg.as_string())
        print("✅ Weekly investor report emailed.")
    except Exception as e:
        print("❌ Email failed:", e)