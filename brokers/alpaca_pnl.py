import os
import alpaca_trade_api as tradeapi
from datetime import datetime
import json

def get_alpaca_pnl(api_key, secret_key, base_url="https://paper-api.alpaca.markets"):
    api = tradeapi.REST(api_key, secret_key, base_url, api_version='v2')
    today = datetime.now().date().isoformat()
    pnl_by_symbol = {}

    activities = api.get_activities(activity_types="FILL")
    for act in activities:
        if act.transaction_time.date().isoformat() != today:
            continue
        symbol = act.symbol
        qty = float(act.qty)
        price = float(act.price)
        side = act.side
        cost = qty * price * (-1 if side == 'buy' else 1)

        if symbol not in pnl_by_symbol:
            pnl_by_symbol[symbol] = 0.0
        pnl_by_symbol[symbol] += cost

    return pnl_by_symbol

if __name__ == "__main__":
    # Replace with your Alpaca keys or load from env
    API_KEY = os.getenv("ALPACA_API_KEY")
    SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")

    pnl = get_alpaca_pnl(API_KEY, SECRET_KEY)
    print("📈 Alpaca Realized PnL Today:")
    for symbol, val in pnl.items():
        print(f"{symbol}: ${round(val, 2)}")
