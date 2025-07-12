"""
Fuses high-performing strategies into a dynamic composite allocation
with protection against alpha decay.
"""

def fuse_alphas(strategy_scores, decay_factor=0.9, surge_threshold=1.5):
    """
    Returns normalized weights based on Sharpe scores.

    Parameters:
    - strategy_scores: dict of {strategy_name: sharpe}
    - decay_factor: multiplier for non-surging strategies
    - surge_threshold: minimum Sharpe for surge qualification

    Returns:
    - dict of {strategy_name: normalized_weight}
    """
    fused = {}
    total = 0

    for name, score in strategy_scores.items():
        if score >= surge_threshold:
            adjusted = score
        elif score > 0:
            adjusted = score * decay_factor
        else:
            adjusted = 0

        if adjusted > 0:
            fused[name] = adjusted
            total += adjusted

    if total > 0:
        for name in fused:
            fused[name] /= total

    return fused