import pandas as pd
from strategies.strategy_base import StrategyBase

class MACD:
    def __init__(self, name=None, config=None):
        self.name = name or "macd"
        self.config = config or {}

        # Default MACD parameters (can be overridden by self.config)
        self.short_window = self.config.get("short_window", 12)
        self.long_window = self.config.get("long_window", 26)
        self.signal_window = self.config.get("signal_window", 9)

    def set_params(self, params):
        if not hasattr(self, "config"):
            self.config = {}
        self.config.update(params)

        self.short_window = self.config.get("short_window", self.short_window)
        self.long_window = self.config.get("long_window", self.long_window)
        self.signal_window = self.config.get("signal_window", self.signal_window)

    def train(self, data):
        pass

    def generate_signal(self, market_data):
        import pandas as pd
        if isinstance(market_data, pd.DataFrame):
            market_data = market_data.copy()  # prevent SettingWithCopyWarning

            market_data["short_ema"] = market_data["close"].ewm(span=self.short_window, adjust=False).mean()
            market_data["long_ema"] = market_data["close"].ewm(span=self.long_window, adjust=False).mean()
            market_data["macd"] = market_data["short_ema"] - market_data["long_ema"]
            market_data["signal_line"] = market_data["macd"].ewm(span=self.signal_window, adjust=False).mean()

            return market_data.apply(
                lambda row: "buy" if row["macd"] > row["signal_line"]
                else "sell" if row["macd"] < row["signal_line"]
                else "hold", axis=1
            )

        elif isinstance(market_data, dict):
            return "hold"  # fallback