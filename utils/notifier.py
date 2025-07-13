import smtplib

def send_email(subject, message, to_email):
    # Placeholder: use proper auth handling in production
    print(f"📧 Alert to {to_email}: {subject} — {message}")