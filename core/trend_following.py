from core.strategy_base import StrategyBase

class TrendFollowingStrategy(StrategyBase):
    def generate_signal(self, market_data):
        price = market_data.get("price", 0)
        ma = market_data.get("ma", 0)
        if price > ma:
            return "buy"
        elif price < ma:
            return "sell"
        return "hold"