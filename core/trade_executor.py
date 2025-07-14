class TradeExecutor:
    def __init__(self, broker_api):
        self.broker = broker_api

    def execute_trade(self, symbol: str, action: str, size: float):
        if action == "buy":
            self.broker.buy(symbol, size)
        elif action == "sell":
            self.broker.sell(symbol, size)
