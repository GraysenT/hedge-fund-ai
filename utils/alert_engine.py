import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client

def send_email_alert(subject, message, recipient):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = "hedgefundai@yourdomain.com"
    msg["To"] = recipient
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("your_email", "your_app_password")
        server.sendmail(msg["From"], [msg["To"]], msg.as_string())

def send_sms_alert(message, to_number):
    client = Client("TWILIO_SID", "TWILIO_AUTH")
    client.messages.create(
        body=message,
        from_="+1234567890",
        to=to_number
    )