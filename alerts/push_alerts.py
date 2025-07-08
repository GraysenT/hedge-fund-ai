import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_push(subject, message):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = os.getenv("YOUR_PHONE_NUMBER")  # E.g., 1234567890@vtext.com
    msg.set_content(message)

    with smtplib.SMTP_SSL("smtp.mail.me.com", 465) as smtp:
        smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
        smtp.send_message(msg)

    print("📱 Push alert sent!")
