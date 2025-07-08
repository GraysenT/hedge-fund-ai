import os
import json
from datetime import datetime

def log_strategy_trade(strategy, symbol, capital_allocated, direction, notes=""):
    log_entry = {
        "strategy": strategy,
        "symbol": symbol,
        "capital": capital_allocated,
        "direction": direction,
        "timestamp": datetime.now().isoformat(),
        "notes": notes
    }

    folder = "memory/trade_logs"
    os.makedirs(folder, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    path = os.path.join(folder, f"{date_str}.json")

    if os.path.exists(path):
        with open(path, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(log_entry)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"📝 Logged trade: {strategy} → {symbol} | ${capital_allocated} | {direction}")
    