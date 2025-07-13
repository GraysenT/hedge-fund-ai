import numpy as np

def calculate_sharpe_ratio(profits, risk_free_rate=0):
    """Calculate Sharpe ratio based on profit/loss data."""
    return np.mean(profits - risk_free_rate) / np.std(profits)