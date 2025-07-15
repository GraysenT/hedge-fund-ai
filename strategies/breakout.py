from core.strategy_base import StrategyBase

class Breakout:
    def __init__(self, name=None, config=None):
        self.name = name or "breakout"
        self.config = config or {}

    def train(self, data):
        # Placeholder — can evolve later
        pass

    def generate_signal(self, market_data):
        import pandas as pd
        if isinstance(market_data, pd.DataFrame):
            return market_data.apply(
                lambda row: "buy" if row.get("price", 0) > row.get("recent_high", 0)
                else "sell" if row.get("price", 0) < row.get("recent_low", 0)
                else "hold",
                axis=1
            )
        elif isinstance(market_data, dict):
            p = market_data.get("price", 0)
            return "buy" if p > market_data.get("recent_high", 0) else \
                   "sell" if p < market_data.get("recent_low", 0) else "hold"
        else:
            raise ValueError("Invalid market_data input")
    
    def set_params(self, params):
        self.config.update(params)