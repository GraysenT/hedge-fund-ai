from execution.live_crypto import CryptoExecutor
from execution.safe_trade_router import SafeTradeRouter

api_key = "your_binance_api_key"
secret = "your_binance_secret"
executor = CryptoExecutor(api_key, secret)
safe_router = SafeTradeRouter(executor)

def deploy_signal(signal, symbol, price, balance=10000):
    if signal in ["buy", "sell"]:
        size = 0.01  # position sizing logic can evolve
        safe_router.safe_execute(symbol, signal, size, price, balance)