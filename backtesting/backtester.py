from sklearn.model_selection import TimeSeriesSplit

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
        data = pd.DataFrame(np.random.randn(100, 1), columns=[symbol])  # Dummy data
        return data

    def walk_forward_analysis(self, data, strategy, num_splits=5):
        """Perform walk-forward validation."""
        tscv = TimeSeriesSplit(n_splits=num_splits)
        for train_index, test_index in tscv.split(data):
            train, test = data[train_index], data[test_index]
            
            # Train strategy on the training data
            strategy.train(train)
            
            # Test strategy on the out-of-sample (test) data
            predictions = strategy.get_signal(test)
            sharpe_ratio = self.calculate_sharpe_ratio(predictions, test)
            print(f"Sharpe Ratio for {strategy.__class__.__name__} (walk-forward): {sharpe_ratio}")

    def calculate_sharpe_ratio(self, profits, test_data=None):
        """Calculate Sharpe ratio based on profit/loss."""
        return np.mean(profits) / np.std(profits)  # Simplified Sharpe Ratio calculation