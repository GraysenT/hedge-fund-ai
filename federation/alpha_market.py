import json
import os
from datetime import datetime

MARKET_FILE = "federation/alpha_marketplace.json"

def list_strategy(strategy, price, duration, description):
    market = json.load(open(MARKET_FILE)) if os.path.exists(MARKET_FILE) else {}
    market[strategy] = {
        "price": price,
        "duration_days": duration,
        "description": description,
        "listed_on": datetime.now().isoformat(),
        "access_count": 0
    }
    with open(MARKET_FILE, "w") as f:
        json.dump(market, f, indent=2)
    print(f"📈 Strategy {strategy} listed on alpha market.")

def access_strategy(strategy):
    market = json.load(open(MARKET_FILE))
    if strategy in market:
        market[strategy]["access_count"] += 1
        with open(MARKET_FILE, "w") as f:
            json.dump(market, f, indent=2)
        print(f"✅ Access granted to {strategy}. Usage recorded.")
    else:
        print("❌ Strategy not listed.")

if __name__ == "__main__":
    list_strategy("gen_strat_r5", 120, 7, "Short-term LSTM breakout strategy")
    access_strategy("gen_strat_r5")
    