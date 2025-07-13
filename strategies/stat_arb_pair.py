from core.strategy_base import StrategyBase

class StatArbPairStrategy(StrategyBase):
    def __init__(self, name, parameters):
        super().__init__(name, parameters)
        self.symbol1 = parameters.get("symbol1", "AAPL")
        self.symbol2 = parameters.get("symbol2", "MSFT")

    def generate_signal(self, market_data):
        s1 = market_data.get(self.symbol1, {}).get("price", 0)
        s2 = market_data.get(self.symbol2, {}).get("price", 0)
        spread = s1 - s2
        mean_spread = market_data.get("spread_mean", 0)
        std_spread = market_data.get("spread_std", 1)

        z = (spread - mean_spread) / std_spread
        if z > 1:
            return "sell"
        elif z < -1:
            return "buy"
        return "hold"