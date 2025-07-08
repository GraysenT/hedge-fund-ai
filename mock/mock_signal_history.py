import json
import os
from datetime import datetime, timedelta
import random

strategies = ["gen_strat_r2", "gen_strat_r3"]
symbols = ["AAPL", "TSLA", "MSFT"]

signal_data = {}

now = datetime.now()
for strat in strategies:
    signal_data[strat] = []
    for i in range(5):
        ts = (now - timedelta(days=i)).strftime("%Y-%m-%d %H:%M:%S")
        symbol = random.choice(symbols)
        direction = random.choice(["buy", "sell"])
        signal_data[strat].append({
            "symbol": symbol,
            "timestamp": ts,
            "action": direction
        })

os.makedirs("memory", exist_ok=True)
with open("memory/signal_history.json", "w") as f:
    json.dump(signal_data, f, indent=2)

print("✅ Mock signal_history.json created with signals for:", strategies)
