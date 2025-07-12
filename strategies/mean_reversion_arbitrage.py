# strategies/mean_reversion_arbitrage.py

import numpy as np
import pandas as pd
from scipy.stats import zscore

class MeanReversionArbitrage:
    def __init__(self, window_size, z_score_threshold):
        self.window_size = window_size
        self.z_score_threshold = z_score_threshold

    def calculate_z_score(self, series):
        return (series - series.mean()) / np.std(series)

    def generate_signals(self, data):
        # Calculate rolling mean and standard deviation
        data['rolling_mean'] = data['Close'].rolling(window=self.window_size).mean()
        data['rolling_std_dev'] = data['Close'].rolling(window=self.window_size).std()

        # Calculate z-score for each day
        data['z_score'] = (data['Close'] - data['rolling_mean']) / data['rolling_std_dev']

        # Generate signals based on z-score
        data['signal'] = 0
        data.loc[data['z_score'] > self.z_score_threshold, 'signal'] = -1
        data.loc[data['z_score'] < -self.z_score_threshold, 'signal'] = 1

        return data

    def execute_trades(self, data):
        # Calculate daily returns
        data['daily_returns'] = data['Close'].pct_change()

        # Calculate strategy returns
        data['strategy_returns'] = data['daily_returns'] * data['signal'].shift()

        return data