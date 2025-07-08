import os
from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv

load_dotenv()

def send_email(subject, body, to=None):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = to or os.getenv("EMAIL_USER")
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.mail.me.com", 465) as smtp:
            smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
            smtp.send_message(msg)
        print("📬 Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

