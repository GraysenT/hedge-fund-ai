import datetime
import random


def send_nightly_email():
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    trades = random.randint(3, 7)
    pnl = round(random.uniform(-300, 1000), 2)
    status = "✅ PROFITABLE" if pnl > 0 else "🔻 LOSS"

    print("📊 [LOG-ONLY MODE] Nightly Trade Summary Email:")
    print("-----------------------------------------------")
    print(f"Subject: 📊 Daily Trade Summary – {date}")
    print("Body:\n")
    print(f"Total trades executed: {trades}")
    print(f"Net PnL: ${pnl}")
    print(f"Status: {status}")
