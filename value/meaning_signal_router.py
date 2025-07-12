def route_signal_by_meaning(signal, beliefs):
    """
    Routes signal activation based on value alignment and strategic belief fit.
    """
    meaning = signal.get("doctrine")
    if meaning in beliefs.get("preferred_strategies", []):
        signal["activation_status"] = "prioritized"
    else:
        signal["activation_status"] = "muted"
    return signal