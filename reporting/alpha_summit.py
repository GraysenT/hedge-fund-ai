import smtplib
import os
import json
from email.message import EmailMessage
from datetime import datetime

EMAIL = os.getenv("EMAIL_USER")
PASS = os.getenv("EMAIL_PASS")

def gather_summary():
    perf = sorted(os.listdir("memory/performance"))[-1]
    pnl = json.load(open(f"memory/performance/{perf}"))

    top_strats = sorted(pnl.items(), key=lambda x: x[1]["pnl"], reverse=True)[:3]
    summary = [f"📊 Weekly Alpha Summary – {datetime.now().strftime('%Y-%m-%d')}"]
    summary.append("\nTop Strategies:")
    for s, r in top_strats:
        summary.append(f" - {s}: ${round(r['pnl'],2)}")

    plugins = json.load(open("plugins/plugin_log.json"))
    for k, v in plugins.items():
        summary.append(f"\nPlugin: {k} → Result: {v.get('result', 'None')}")

    return "\n".join(summary)

def send_summary():
    msg = EmailMessage()
    msg["Subject"] = "🧠 Weekly Alpha Summit"
    msg["From"] = EMAIL
    msg["To"] = EMAIL
    msg.set_content(gather_summary())

    with smtplib.SMTP_SSL("smtp.mail.me.com", 465) as smtp:
        smtp.login(EMAIL, PASS)
        smtp.send_message(msg)

    print("📨 Alpha summit sent.")

if __name__ == "__main__":
    send_summary()
    