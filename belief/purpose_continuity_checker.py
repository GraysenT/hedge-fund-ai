def check_purpose_drift(current_purpose, historical_purposes):
    """
    Detects if a strategy has drifted too far from its original stated goal.
    """
    if not historical_purposes:
        return False
    drift_score = sum(
        1 for past in historical_purposes
        if past.strip().lower() != current_purpose.strip().lower()
    )
    return drift_score > len(historical_purposes) * 0.5