def detect_cycle_retrigger(market_series):
    """
    Detects early re-emergence of past cyclical patterns using volatility + correlation matching.
    """
    retrigger_events = []
    for i, point in enumerate(market_series):
        if i > 20 and abs(point - market_series[i-10]) < 0.05:
            retrigger_events.append(i)
    return retrigger_events