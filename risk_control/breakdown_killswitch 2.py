```python
# File: risk_control/breakdown_killswitch.py

import pandas as pd

class BreakdownKillSwitch:
    def __init__(self, strategy_performance, threshold):
        """
        Initialize the BreakdownKillSwitch with strategy performance data and threshold for underperformance.

        :param strategy_performance: A pandas DataFrame containing strategy performance data.
        :param threshold: A float indicating the threshold for underperformance.
        """
        self.strategy_performance = strategy_performance
        self.threshold = threshold
        self.strategy_status = {strategy: True for strategy in strategy_performance.columns}

    def check_strategy_performance(self):
        """
        Check the performance of each strategy and disable it if it underperforms.
        """
        for strategy in self.strategy_performance.columns:
            if self.strategy_performance[strategy].iloc[-1] < self.threshold:
                self.strategy_status[strategy] = False

    def get_strategy_status(self):
        """
        Get the status of each strategy.

        :return: A dictionary containing the status of each strategy.
        """
        return self.strategy_status


# Example usage:

# Create a DataFrame with strategy performance data
strategy_performance = pd.DataFrame({
    'strategy1': [0.1, 0.2, -0.3, -0.4, -0.5],
    'strategy2': [0.1, 0.2, 0.3, 0.4, 0.5],
    'strategy3': [0.1, -0.2, -0.3, -0.4, -0.5]
})

# Initialize the BreakdownKillSwitch with the strategy performance data and a threshold of -0.3
kill_switch = BreakdownKillSwitch(strategy_performance, -0.3)

# Check the performance of each strategy
kill_switch.check_strategy_performance()

# Get the status of each strategy
strategy_status = kill_switch.get_strategy_status()

# Print the status of each strategy
for strategy, status in strategy_status.items():
    print(f'Strategy: {strategy}, Status: {"Active" if status else "Disabled"}')
```