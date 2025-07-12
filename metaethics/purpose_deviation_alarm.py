def detect_mission_drift(strategy, current_manifest):
    """
    Raises alarm if a strategy's recent behavior diverges from stated purpose.
    """
    stated = strategy.get("purpose", "")
    for line in current_manifest:
        if stated in line:
            return False
    return True