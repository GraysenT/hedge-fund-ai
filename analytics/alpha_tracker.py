```python
# analytics/alpha_tracker.py

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

class AlphaTracker:
    def __init__(self, strategies):
        self.strategies = strategies
        self.alpha_data = {strategy: [] for strategy in strategies}

    def track_alpha(self, strategy, alpha, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now()
        self.alpha_data[strategy].append((timestamp, alpha))

    def get_alpha_data(self, strategy):
        return pd.DataFrame(self.alpha_data[strategy], columns=['timestamp', 'alpha'])

    def plot_alpha(self, strategy):
        data = self.get_alpha_data(strategy)
        plt.plot(data['timestamp'], data['alpha'])
        plt.title(f'Alpha over time for {strategy}')
        plt.xlabel('Timestamp')
        plt.ylabel('Alpha')
        plt.show()

    def calculate_drift(self, strategy):
        data = self.get_alpha_data(strategy)
        data['drift'] = data['alpha'].diff()
        return data

    def plot_drift(self, strategy):
        data = self.calculate_drift(strategy)
        plt.plot(data['timestamp'], data['drift'])
        plt.title(f'Drift over time for {strategy}')
        plt.xlabel('Timestamp')
        plt.ylabel('Drift')
        plt.show()

# Example usage:
if __name__ == "__main__":
    tracker = AlphaTracker(['strategy1', 'strategy2'])
    tracker.track_alpha('strategy1', 0.05)
    tracker.track_alpha('strategy2', 0.03)
    tracker.plot_alpha('strategy1')
    tracker.plot_drift('strategy2')
```