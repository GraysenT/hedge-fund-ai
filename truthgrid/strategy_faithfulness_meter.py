def measure_faithfulness(strategy):
    """
    Checks whether a strategy still acts in accordance with its declared belief system.
    """
    declared = strategy.get("belief", "")
    behavior = strategy.get("last_actions", [])
    faithfulness = sum(1 for a in behavior if declared in a) / max(1, len(behavior))
    return round(faithfulness, 2)