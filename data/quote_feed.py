import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

load_dotenv()

ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
ALPACA_BASE_URL = os.getenv("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")

api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, base_url=ALPACA_BASE_URL)

def get_latest_price(ticker="AAPL"):
    try:
        if ticker.upper() in ["BTC/USD", "ETH/USD"]:
            bars = api.get_crypto_bars(ticker, timeframe="1Min", limit=1).df
        else:
            bars = api.get_bars(ticker, timeframe="1Min", limit=1).df

        if bars.empty:
            return None

        last = float(bars["close"].iloc[-1])
        return {
            "ticker": ticker,
            "last": last,
            "source": "Alpaca"
        }
    except Exception as e:
        print(f"❌ Alpaca quote failed for {ticker}: {e}")
        return None

if __name__ == "__main__":
    print(get_latest_price("AAPL"))
    print(get_latest_price("BTC/USD"))