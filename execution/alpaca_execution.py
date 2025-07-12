import alpaca_trade_api as tradeapi

class AlpacaExecution:
    def __init__(self, api_key, secret_key, paper=True):
        self.api_key = api_key
        self.secret_key = secret_key
        self.paper = paper
        base_url = "https://paper-api.alpaca.markets" if paper else "https://api.alpaca.markets"
        self.api = tradeapi.REST(self.api_key, self.secret_key, base_url, api_version='v2')

    def place_order(self, symbol, qty, side, order_type='market', time_in_force='gtc'):
        """Place an order on Alpaca for stocks, ETFs, commodities, or cryptos."""
        try:
            order = self.api.submit_order(
                symbol=symbol,
                qty=qty,
                side=side,
                type=order_type,
                time_in_force=time_in_force
            )
            print(f"Placed {side} order for {qty} {symbol} at {order_type} price.")
            return order
        except Exception as e:
            print(f"Error placing order: {e}")
            return None