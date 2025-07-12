```python
import numpy as np

def block_signals(signals, volatility_threshold, confidence_threshold, regime_actual, regime_desired):
    """
    Blocks signals based on volatility, confidence, and regime match criteria.

    Parameters:
    - signals (list of dict): List of signals where each signal is a dictionary with keys 'value', 'volatility', 'confidence', and 'regime'.
    - volatility_threshold (float): Maximum allowed volatility for the signals.
    - confidence_threshold (float): Minimum required confidence for the signals.
    - regime_actual (str): The actual regime of the environment.
    - regime_desired (str): The desired regime for the signals to be effective.

    Returns:
    - list of dict: Filtered signals that meet the criteria.
    """
    filtered_signals = []
    for signal in signals:
        if (signal['volatility'] <= volatility_threshold and
            signal['confidence'] >= confidence_threshold and
            signal['regime'] == regime_desired and
            regime_actual == regime_desired):
            filtered_signals.append(signal)
    return filtered_signals

# Example usage:
signals = [
    {'value': 100, 'volatility': 0.5, 'confidence': 0.8, 'regime': 'bull'},
    {'value': 200, 'volatility': 0.3, 'confidence': 0.9, 'regime': 'bear'},
    {'value': 150, 'volatility': 0.7, 'confidence': 0.6, 'regime': 'bull'},
    {'value': 120, 'volatility': 0.2, 'confidence': 0.95, 'regime': 'bull'}
]

volatility_threshold = 0.4
confidence_threshold = 0.7
regime_actual = 'bull'
regime_desired = 'bull'

filtered_signals = block_signals(signals, volatility_threshold, confidence_threshold, regime_actual, regime_desired)
print(filtered_signals)
```