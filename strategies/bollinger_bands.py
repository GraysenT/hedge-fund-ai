import pandas as pd
from strategies.strategy_base import StrategyBase

class BollingerBands:
    def __init__(self, name=None, config=None):
        self.name = name or "bollinger_bands"
        self.config = config or {}

    def train(self, data):
        # Placeholder for backtester compatibility
        pass

    def generate_signal(self, market_data):
        import pandas as pd

        if isinstance(market_data, pd.DataFrame):
            if "price" not in market_data.columns:
                raise ValueError("Missing 'price' column in BollingerBands strategy")

            rolling_mean = market_data["price"].rolling(window=20).mean()
            rolling_std = market_data["price"].rolling(window=20).std()

            upper_band = rolling_mean + (2 * rolling_std)
            lower_band = rolling_mean - (2 * rolling_std)

            return market_data.apply(
                lambda row: "buy" if row["price"] < lower_band[row.name]
                else "sell" if row["price"] > upper_band[row.name]
                else "hold", axis=1
            )

        elif isinstance(market_data, dict):
            return "hold"  # basic fallback
    
    def set_params(self, params):
        self.config.update(params)