import os
import alpaca_trade_api as tradeapi
from dotenv import load_dotenv

load_dotenv()

ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
ALPACA_BASE_URL = os.getenv("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")

api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, base_url=ALPACA_BASE_URL)

def place_alpaca_order(asset, qty=1, side="buy"):
    try:
        order = api.submit_order(
            symbol=asset,
            qty=qty,
            side=side,
            type="market",
            time_in_force="gtc"
        )
        print(f"✅ Alpaca order placed: {side.upper()} {qty} {asset}")
        return order
    except Exception as e:
        print(f"❌ Alpaca order failed: {e}")
        return None