from core.strategy_base import StrategyBase

class TrendFollowingStrategy(StrategyBase):
    """
    A simple trend-following strategy that compares price vs. moving average.
    If price > MA → Buy. If price < MA → Sell. Otherwise → Hold.
    """

    def generate_signal(self, market_data):
        try:
            price = float(market_data.get("price", 0))
            ma = float(market_data.get("ma", 0))

            if ma == 0:
                return "hold"

            if price > ma:
                return "buy"
            elif price < ma:
                return "sell"
            else:
                return "hold"

        except Exception as e:
            print(f"[TrendFollowingStrategy] Error generating signal: {e}")
            return "hold"