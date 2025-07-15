import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
from registry.agent_registry import AgentRegistry
from logs.sharpe_logger import log_sharpe
log_sharpe(agent.name, sharpe_ratio)

...

agent = strategy_instance
agent.sharpe_score = calculated_sharpe
AgentRegistry.register("backtest_" + strategy.__class__.__name__, agent)

class Backtester:
    def __init__(self, strategies):
        self.strategies = strategies
    
    def run_backtest(self):
        """Run backtest for all strategies."""
        for strategy in self.strategies:
            self.test_strategy(strategy)
    
    def test_strategy(self, strategy):
        """Test a given strategy."""
        # Simulate fetching historical data
        historical_data = self.get_historical_data("AAPL")
        
        # Walk-forward analysis using TimeSeriesSplit
        self.walk_forward_analysis(historical_data, strategy)

    def get_historical_data(self, symbol):
        """Simulate fetching historical data."""
        data = pd.DataFrame(np.random.randn(100, 1), columns=["close"])
        data["short_ema"] = data["close"].ewm(span=12, adjust=False).mean()
        data["long_ema"] = data["close"].ewm(span=26, adjust=False).mean()
        data["macd"] = data["short_ema"] - data["long_ema"]
        data["signal"] = data["macd"].ewm(span=9, adjust=False).mean()

        # Also include defaults for other strategies
        data["price"] = data["close"]
        data["moving_average"] = data["price"].rolling(window=20).mean().fillna(data["price"])
        data["momentum"] = data["price"].diff().fillna(0)
        data["recent_high"] = data["price"].rolling(window=5).max().fillna(data["price"])
        data["recent_low"] = data["price"].rolling(window=5).min().fillna(data["price"])
        return data

    def walk_forward_analysis(self, data, strategy, num_splits=5):
        """Perform walk-forward validation."""
        tscv = TimeSeriesSplit(n_splits=num_splits)
        for train_index, test_index in tscv.split(data):
            train, test = data.iloc[train_index], data.iloc[test_index]
            
            # Train strategy on the training data
            strategy.train(train)
            
            # Test strategy on the out-of-sample (test) data
            predictions = strategy.generate_signal(test)
            sharpe_ratio = self.calculate_sharpe_ratio(predictions, test)
            print(f"Sharpe Ratio for {strategy.__class__.__name__} (walk-forward): {sharpe_ratio}")

    def calculate_sharpe_ratio(self, predictions, test_data):
        import pandas as pd

        # Convert to Series if it's a list
        if not isinstance(predictions, pd.Series):
            predictions = pd.Series(predictions)

        mapped_profits = predictions.map({
            "buy": 1,
            "sell": -1
        }).fillna(0)

        if mapped_profits.empty or mapped_profits.std() == 0:
            return 0

        return mapped_profits.mean() / mapped_profits.std()