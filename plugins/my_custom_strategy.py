from core.strategy_base import StrategyBase

class MyCustomStrategy(StrategyBase):
    def generate_signal(self, market_data):
        if market_data["price"] > market_data["ma"]:
            return "buy"
        return "sell"