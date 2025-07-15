import pandas as pd
import numpy as np
from core.strategy_base import StrategyBase

class TrendFollowing:
    def __init__(self, name=None, config=None):
        self.name = name or "trend_following"
        self.config = config or {}

    def generate_signal(self, market_data):
        if isinstance(market_data, pd.DataFrame):
            # Generate one prediction per row
            return market_data.apply(
                lambda row: "buy" if row["price"] > row["moving_average"] else "sell",
                axis=1
            )
        elif isinstance(market_data, dict):
            return "buy" if market_data["price"] > market_data["moving_average"] else "sell"
        else:
            raise ValueError("Invalid input type for market_data.")
    
    def train(self, data):
        # Optional: strategy-specific training logic
        pass

    def set_params(self, params):
        self.config.update(params)
    
    def get_signal(self, market_data):
        return self.generate_signal(market_data)