Below is a Python script that monitors alpha erosion and volatility, sending warnings when certain thresholds are exceeded. This example assumes you have a way to calculate or retrieve alpha and volatility values, possibly from financial data. The script uses a simple polling mechanism to check these metrics at regular intervals and sends a warning if they exceed predefined limits.

```python
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration for email
email_sender = 'your_email@example.com'
email_password = 'your_password'
email_receiver = 'receiver_email@example.com'

# SMTP server configuration
smtp_server = 'smtp.example.com'
smtp_port = 587

# Thresholds
alpha_threshold = 0.02  # Example threshold for alpha erosion
volatility_threshold = 0.30  # Example threshold for high volatility

def send_email(subject, message):
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_sender, email_password)
    text = msg.as_string()
    server.sendmail(email_sender, email_receiver, text)
    server.quit()

def check_metrics():
    # Dummy values for alpha and volatility
    # In practice, replace these with actual data retrieval and computation logic
    alpha = 0.015  # Example alpha value
    volatility = 0.35  # Example volatility value

    warnings = []

    if alpha < alpha_threshold:
        warnings.append(f"Warning: Alpha erosion detected. Current alpha: {alpha}")

    if volatility > volatility_threshold:
        warnings.append(f"Warning: High volatility detected. Current volatility: {volatility}")

    return warnings

def main():
    while True:
        warnings = check_metrics()
        if warnings:
            for warning in warnings:
                print(warning)
                send_email("Market Alert", warning)
        time.sleep(3600)  # Check every hour

if __name__ == "__main__":
    main()
```

### Explanation:
1. **Email Configuration**: Set up your email details and SMTP server information. Make sure to replace placeholders with your actual email credentials and server details.
2. **Thresholds**: Define the thresholds for alpha erosion and high volatility.
3. **Sending Emails**: The `send_email` function handles the creation and sending of emails.
4. **Checking Metrics**: The `check_metrics` function simulates the retrieval and checking of alpha and volatility against the thresholds. Replace dummy values with actual data retrieval logic.
5. **Main Loop**: The script continuously checks the metrics at regular intervals (every hour in this example) and sends warnings via email if any thresholds are exceeded.

### Note:
- Ensure you have the correct permissions and settings configured on your SMTP server to send emails.
- Replace dummy data retrieval in `check_metrics` with actual financial data processing logic.
- Handle network errors and authentication issues in a production environment for robustness.