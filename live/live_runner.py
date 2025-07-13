from core.market_data_feed import MarketDataFeed
from execution.live_crypto import CryptoExecutor
from execution.safe_trade_router import SafeTradeRouter
import time

api_key = "your_binance_api_key"
secret = "your_binance_secret"

feed = MarketDataFeed(data_sources=["binance"])
executor = CryptoExecutor(api_key, secret)
safe = SafeTradeRouter(executor)

balance = 10000
symbol = "ETH/USDT"

while True:
    data = feed.fetch(symbol)
    price = data["price"]
    signal = "buy" if price < 1800 else "sell"  # placeholder logic
    safe.safe_execute(symbol, signal, 0.01, price, balance)
    time.sleep(60)