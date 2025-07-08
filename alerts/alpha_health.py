import smtplib
from email.mime.text import MIMEText

class AlphaHealthNotifier:
    def __init__(self, recipient_email):
        self.recipient_email = recipient_email

    def send_alert(self, strategy, score, status):
        subject = f"ALPHA STATUS: {strategy} is now {status.upper()}"
        body = f"Strategy '{strategy}' has a score of {score:.2f} and is now {status}."
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = "alerts@hedgefundai.com"
        msg["To"] = self.recipient_email

        try:
            with smtplib.SMTP("localhost") as server:
                server.send_message(msg)
            print(f"[ALERT SENT] {subject}")
        except Exception as e:
            print(f"[ALERT ERROR] Could not send alert: {e}")
