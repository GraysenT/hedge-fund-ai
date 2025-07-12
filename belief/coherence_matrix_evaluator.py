def evaluate_coherence_matrix(strategies):
    """
    Checks for alignment between strategy logic, belief statements, and behavior.
    Returns matrix of scores: [0.0–1.0]
    """
    results = {}
    for strat in strategies:
        belief = strat.get("belief", "")
        logic = strat.get("logic", "")
        purpose = strat.get("purpose", "")
        match = 1.0

        if belief not in logic:
            match -= 0.4
        if purpose not in logic:
            match -= 0.4

        results[strat["name"]] = max(0.0, match)
    return results