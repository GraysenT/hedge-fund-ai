import pandas as pd

class MomentumBased:
    def __init__(self, roc_period=14):
        self.roc_period = roc_period

    def get_signal(self, live_data):
        """Get buy or sell signal based on momentum strategy."""
        prices = live_data["AAPL"]

        # Calculate Rate of Change (ROC)
        roc = (prices - prices.shift(self.roc_period)) / prices.shift(self.roc_period) * 100

        # Calculate RSI (Relative Strength Index)
        delta = prices.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        # Buy signal when momentum is positive and RSI is not overbought
        if roc[-1] > 0 and rsi[-1] < 70:
            return "buy"
        # Sell signal when momentum is negative and RSI is not oversold
        elif roc[-1] < 0 and rsi[-1] > 30:
            return "sell"
        return "hold"
    
    def set_params(self, params):
        """Set optimized parameters for the strategy."""
        self.roc_period = params.get('roc_period', self.roc_period)

class MomentumBased:
    def __init__(self, name=None, config=None):
        self.name = name or "momentum_based"
        self.config = config or {}

    def generate_signal(self, market_data):
        if isinstance(market_data, pd.DataFrame):
            if "momentum" not in market_data.columns:
                market_data["momentum"] = 0  # default fallback

            return market_data.apply(
                lambda row: "buy" if row["momentum"] > 0 else "sell",
                axis=1
            )

        elif isinstance(market_data, dict):
            return "buy" if market_data.get("momentum", 0) > 0 else "sell"

        else:
            raise ValueError("Invalid input for momentum strategy.")
        
    def train(self, data):
        # Optional: strategy-specific training logic
        pass

    def set_params(self, params):
        self.config.update(params)