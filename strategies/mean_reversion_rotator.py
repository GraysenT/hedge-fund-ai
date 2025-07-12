# strategies/mean_reversion_rotator.py

import numpy as np
import pandas as pd
from scipy.stats import zscore

class MeanReversionRotator:
    def __init__(self, lookback, z_score_threshold):
        self.lookback = lookback
        self.z_score_threshold = z_score_threshold

    def compute_signals(self, data):
        """
        Compute trading signals based on mean reversion strategy
        """
        # Calculate rolling mean and standard deviation
        data['rolling_mean'] = data['Close'].rolling(window=self.lookback).mean()
        data['rolling_std'] = data['Close'].rolling(window=self.lookback).std()

        # Calculate z-score for each day
        data['z_score'] = (data['Close'] - data['rolling_mean']) / data['rolling_std']

        # Create signals based on z-score
        data['signal'] = np.where(data['z_score'] > self.z_score_threshold, -1, 0)
        data['signal'] = np.where(data['z_score'] < -self.z_score_threshold, 1, data['signal'])

        return data

    def execute_trades(self, data):
        """
        Execute trades based on the signals
        """
        # Calculate daily returns
        data['returns'] = data['Close'].pct_change()

        # Calculate strategy returns
        data['strategy_returns'] = data['returns'] * data['signal'].shift()

        return data