import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from sklearn.linear_model import LinearRegression

def detect_signal_decay(signal_data):
    """
    Test if the signal is stationary using the Augmented Dickey-Fuller test.
    A stationary signal is less likely to experience performance decay.
    
    Parameters:
        signal_data (array-like): The time series data of the signal.
        
    Returns:
        bool: True if the signal is stationary, False otherwise.
    """
    result = adfuller(signal_data)
    p_value = result[1]
    return p_value < 0.05  # Signal is stationary if p-value is less than 0.05

def protect_signal(signal_data, window_size=30, threshold=0.05):
    """
    Apply a moving average filter to smooth out short-term fluctuations and protect the signal from external shocks.
    
    Parameters:
        signal_data (array-like): The time series data of the signal.
        window_size (int): The size of the moving window.
        threshold (float): The threshold for detecting non-stationarity.
        
    Returns:
        array-like: The protected signal data.
    """
    if not detect_signal_decay(signal_data):
        print("Signal is non-stationary; applying protection.")
        # Apply moving average to smooth the signal
        protected_signal = pd.Series(signal_data).rolling(window=window_size, min_periods=1).mean()
        return protected_signal
    else:
        print("Signal is stationary; no protection needed.")
        return signal_data

# Example usage:
# Generate a sample non-stationary time series data
np.random.seed(0)
time_series_data = np.random.randn(100).cumsum() + 100  # Cumulative sum to simulate non-stationary data

# Protect the signal
protected_data = protect_signal(time_series_data)
print(protected_data)