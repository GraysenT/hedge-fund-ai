def validate_strategy_theory(strategy, known_truths):
    """
    Tests whether a strategy violates, supports, or mutates system-wide theories.
    """
    for t in known_truths:
        if t in strategy.get("logic", ""):
            return {"validation": "supports", "truth": t}
    return {"validation": "unverified"}