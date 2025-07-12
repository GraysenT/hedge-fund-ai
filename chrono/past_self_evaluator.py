def compare_to_past_versions(current_logic, historical_versions):
    """
    Compares current strategy logic to prior forms for drift, divergence, or redundancy.
    """
    changes = []
    for old in historical_versions:
        if current_logic != old:
            changes.append({"from": old[:60], "to": current_logic[:60]})
    return changes