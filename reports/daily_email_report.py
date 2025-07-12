import os
import smtplib
import pandas as pd
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from utils.snapshot_loader import load_latest_snapshot  # Reuses strategy memory snapshot loader
from utils.config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECIPIENT
from backup.s3_uploader import upload_to_s3  # Added for S3 backup


def generate_report():
    snapshot = load_latest_snapshot()
    date_str = datetime.now().strftime('%Y-%m-%d')

    performance_df = snapshot.get("performance")
    weights_df = snapshot.get("weights")
    status_df = snapshot.get("status")

    html = f"""
    <h2>📬 Daily Alpha Report – {date_str}</h2>
    <h3>📈 Strategy Performance</h3>
    {performance_df.to_html(index=False)}

    <h3>💸 Allocation Weights</h3>
    {weights_df.to_html(index=False)}

    <h3>✅ Strategy Status</h3>
    {status_df.to_html(index=False)}
    """
    return html, snapshot.get("raw_path")


def send_email():
    html, attachment_path = generate_report()

    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECIPIENT
    msg['Subject'] = f"Daily Alpha Summary – {datetime.now().strftime('%B %d, %Y') }"

    msg.attach(MIMEText(html, 'html'))

    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, 'rb') as file:
            part = MIMEApplication(file.read(), Name=os.path.basename(attachment_path))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
            msg.attach(part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)

    print("✅ Daily alpha email sent successfully.")

    if attachment_path:
        upload_to_s3(attachment_path)


if __name__ == '__main__':
    send_email()
