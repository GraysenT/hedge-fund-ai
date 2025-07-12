def track_signal_outcome(signal, result):
    """
    Measures whether the trade resulting from a signal achieved its intended goal.
    """
    intended = signal.get("target_outcome")
    achieved = result.get("actual_outcome")
    return {"alignment": intended == achieved, "details": (intended, achieved)}