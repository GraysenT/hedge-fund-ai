def crossverify_alpha_paths(strategies, universes):
    """
    Confirms whether a strategy’s alpha path remains profitable across divergent realities.
    """
    result = {}
    for strat in strategies:
        scores = strat.get("universe_scores", {})
        result[strat["name"]] = all(score > 0 for score in [scores.get(u, 0) for u in universes])
    return result