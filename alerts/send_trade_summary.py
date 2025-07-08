import smtplib
from email.message import EmailMessage
import json
import os

def send_trade_email(order_log_path):
    with open(order_log_path) as f:
        orders = json.load(f)

    body = "\n".join([f"{o['strategy']} → {o['action'].upper()} {o['qty']} {o['symbol']} @ ${o['price']}" for o in orders])
    subject = f"📈 {len(orders)} Trades Executed — {orders[0]['timestamp'][:10]}"

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = os.getenv("EMAIL_USER")  # or your phone’s email-to-SMS address

    with smtplib.SMTP_SSL("smtp.mail.me.com", 465) as smtp:
        smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
        smtp.send_message(msg)

    print("📬 Trade alert email sent.")
