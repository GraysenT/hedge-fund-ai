import json
import os

ORDERS_PATH = "memory/order_logs"
PRICE_PATH = "data/price_history"

def check_fills():
    latest = sorted(os.listdir(ORDERS_PATH))[-1]
    trades = json.load(open(os.path.join(ORDERS_PATH, latest)))

    for t in trades:
        symbol = t["symbol"]
        entry = float(t["price"])
        price_path = f"{PRICE_PATH}/{symbol}.csv"

        if not os.path.exists(price_path):
            continue

        # Check next day's price
        with open(price_path) as f:
            lines = f.readlines()
        idx = next((i for i, l in enumerate(lines) if t["timestamp"].split("T")[0] in l), -1)
        if idx != -1 and idx + 1 < len(lines):
            next_price = float(lines[idx + 1].split(",")[1])
            pnl = (next_price - entry) if t["action"] == "buy" else (entry - next_price)
            print(f"{t['strategy']} → PnL: {round(pnl, 2)} | Entry: {entry} → Exit: {next_price}")
            