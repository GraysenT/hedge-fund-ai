from binance.client import Client

class BinanceBroker:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)

    def buy(self, symbol: str, qty: float):
        self.client.order_market_buy(symbol=symbol, quantity=qty)

    def sell(self, symbol: str, qty: float):
        self.client.order_market_sell(symbol=symbol, quantity=qty)