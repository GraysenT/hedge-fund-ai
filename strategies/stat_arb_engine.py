import random

def generate_stat_arb_signal(ticker, price):
    """
    Simulated statistical arbitrage signal generator.
    Uses a mock spread and threshold to create a signal.
    """

    # Example logic: simulate mean reversion if price deviates from 100
    reference_mean = 150 if ticker == "AAPL" else 220
    spread = price - reference_mean
    threshold = 5

    # Decision logic
    if spread < -threshold:
        action = "BUY"
        confidence = 0.9
    elif spread > threshold:
        action = "SELL"
        confidence = 0.9
    else:
        action = "HOLD"
        confidence = 0.6

    return {
        "timestamp": None,  # filled by runloop
        "asset": ticker,
        "strategy": "stat_arb",
        "price": price,
        "spread": round(spread, 2),
        "action": action,
        "confidence": confidence
    }

def generate_signal():
    return 'skip'
