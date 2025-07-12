def fuse_alphas(strategy_scores, decay_factor=0.9, surge_threshold=1.5):
    """
    Fuses high-performing strategies with decayed weight for weaker ones.

    Params:
        strategy_scores: dict of {strategy: sharpe}
    Returns:
        dict of {strategy: normalized_weight}
    """
    fused = {}
    total = 0.0

    for strat, score in strategy_scores.items():
        if score >= surge_threshold:
            weight = score
        elif score > 0:
            weight = score * decay_factor
        else:
            weight = 0

        if weight > 0:
            fused[strat] = weight
            total += weight

    if total > 0:
        for strat in fused:
            fused[strat] /= total

    return fused