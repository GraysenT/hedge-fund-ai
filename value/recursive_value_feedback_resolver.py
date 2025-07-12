def resolve_signal_value_alignment(signal, feedback):
    """
    Recursively adjusts belief alignment and priority based on performance and purpose fit.
    """
    score = signal.get("belief_score", 0.5)
    if feedback.get("aligned"):
        score += 0.1
    else:
        score -= 0.1
    signal["belief_score"] = max(0.0, min(1.0, score))
    return signal