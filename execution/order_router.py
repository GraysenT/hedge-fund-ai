from dotenv import load_dotenv
load_dotenv()
import os
import json
from datetime import datetime
import alpaca_trade_api as tradeapi

SIGNAL_PATH = "memory/signal_history.json"
WEIGHTS_PATH = "memory/optimized_weights.json"
DEPLOY_PATH = "strategy_memory/deployment_status.json"

API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = os.getenv("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")  # live URL if switching

BASE_CAPITAL = 1_000_000

def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)

def route_orders(signals, weights, deploy_status):
    api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL)

    executed_orders = []

    for strat, events in signals.items():
        if strat not in weights:
            continue
        if not deploy_status.get(strat, {}).get("approved", False):
            continue

        capital = BASE_CAPITAL * weights[strat]
        for sig in events:
            symbol = sig["symbol"]
            action = sig["action"]
            timestamp = sig["timestamp"]

            try:
                # Fetch latest price
                last = api.get_latest_trade(symbol)
                price = float(last.price)
                qty = round(capital / price)

                if qty == 0:
                    print(f"⚠️ {strat} skipped {symbol} (capital too low)")
                    continue

                # Place order
                order = api.submit_order(
                    symbol=symbol,
                    qty=qty,
                    side=action,
                    type='market',
                    time_in_force='gtc'
                )

                print(f"✅ {strat} → {action.upper()} {qty} {symbol} @ ${price}")
                executed_orders.append({
                    "strategy": strat,
                    "symbol": symbol,
                    "action": action,
                    "qty": qty,
                    "price": price,
                    "timestamp": timestamp,
                    "alpaca_id": order.id
                })

            except Exception as e:
                print(f"❌ Order failed for {strat} → {symbol}: {e}")

    return executed_orders

def save_order_log(executed_orders):
    folder = "memory/order_logs"
    os.makedirs(folder, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d_%H%M")
    path = os.path.join(folder, f"{date_str}.json")
    with open(path, "w") as f:
        json.dump(executed_orders, f, indent=2)
    print(f"\n💾 Order log saved to {path}")

if __name__ == "__main__":
    print("🚀 Live Order Router Starting...\n")
    signals = load_json(SIGNAL_PATH)
    weights = load_json(WEIGHTS_PATH)
    deploy_status = load_json(DEPLOY_PATH)

    if not API_KEY or not SECRET_KEY:
        print("❌ Alpaca API keys missing. Set ALPACA_API_KEY and ALPACA_SECRET_KEY.")
        exit()

    orders = route_orders(signals, weights, deploy_status)
    save_order_log(orders)