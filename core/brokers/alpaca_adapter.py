import alpaca_trade_api as tradeapi

class AlpacaBroker:
    def __init__(self, api_key, api_secret, base_url):
        self.api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

    def buy(self, symbol: str, qty: float):
        self.api.submit_order(symbol=symbol, qty=qty, side='buy', type='market', time_in_force='gtc')

    def sell(self, symbol: str, qty: float):
        self.api.submit_order(symbol=symbol, qty=qty, side='sell', type='market', time_in_force='gtc')