"""
High-frequency execution engine that scalps rapid micro-movements using tick data.
Requires real-time feed with sub-second resolution.
"""

import random

def generate_hft_signal(price_series, threshold=0.03):
    """
    Detects micro spikes and drops for scalping.
    Returns 'buy', 'sell', or None.
    """
    if len(price_series) < 5:
        return None

    recent = price_series[-5:]
    change = (recent[-1] - recent[0]) / recent[0]

    if change > threshold:
        return "sell"
    elif change < -threshold:
        return "buy"
    else:
        return None

def place_hft_order(signal):
    """
    Dummy order placement logic.
    """
    if signal:
        print(f"[HFT] Executing {signal.upper()} order.")