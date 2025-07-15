import pandas as pd
import numpy as np
from core.strategy_base import StrategyBase

class MeanReversion:
    def __init__(self, name=None, config=None):
        self.name = name or "mean_reversion"
        self.config = config or {}

    def train(self, data):
        pass

    def generate_signal(self, market_data):
        if isinstance(market_data, pd.DataFrame):
            # Row-wise signal per time slice
            return market_data.apply(
                lambda row: "buy" if row["price"] < row["moving_average"] else "sell",
                axis=1
            )
        elif isinstance(market_data, dict):
            return "buy" if market_data["price"] < market_data["moving_average"] else "sell"
        else:
            raise ValueError("Invalid input type for market_data")
    
    def set_params(self, params):
        self.config.update(params)