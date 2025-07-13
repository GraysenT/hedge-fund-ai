from core.strategy_base import StrategyBase

class BreakoutStrategy(StrategyBase):
    def generate_signal(self, market_data):
        high = market_data.get("recent_high", 0)
        low = market_data.get("recent_low", 0)
        price = market_data.get("price", 0)
        if price > high:
            return "buy"
        elif price < low:
            return "sell"
        return "hold"