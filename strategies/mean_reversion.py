from core.strategy_base import StrategyBase

class MeanReversionStrategy(StrategyBase):
    def generate_signal(self, market_data):
        price = market_data.get("price", 0)
        upper = market_data.get("upper_band", 0)
        lower = market_data.get("lower_band", 0)
        if price < lower:
            return "buy"
        elif price > upper:
            return "sell"
        return "hold"