def compute_signal_divergence(u1, u2):
    """
    Returns a measure of how divergent two universes are in signal space.
    """
    inflation_gap = abs(u1.inflation - u2.inflation)
    tech_gap = abs(u1.tech_adoption - u2.tech_adoption)
    war_gap = abs(u1.war_risk - u2.war_risk)
    liq_gap = abs(u1.liquidity - u2.liquidity)

    divergence_score = inflation_gap * 0.3 + tech_gap * 0.3 + war_gap * 0.2 + liq_gap * 0.2
    return round(divergence_score, 3)