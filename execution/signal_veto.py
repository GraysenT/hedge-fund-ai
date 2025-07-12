def veto_signal(signal, risk_threshold=0.7, min_confidence=0.2):
    """
    Decide whether to block signal based on risk and confidence.
    """
    if signal.get("confidence", 0) < min_confidence:
        return True

    if signal.get("risk", 0) > risk_threshold:
        return True

    return False