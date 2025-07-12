def infer_signal_doctrine(signal):
    """
    Assigns a belief system or doctrine to the strategy based on its logic structure.
    """
    logic = signal.get("logic", "")
    if "fear" in logic:
        return "volatility_defense"
    elif "trend" in logic:
        return "momentum_follower"
    return "neutral_observer"