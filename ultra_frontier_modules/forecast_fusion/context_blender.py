def blend_context_weights(contexts):
    """
    Converts symbolic contexts into slight forecast modifiers.
    """
    modifiers = {
        "CPI Week": -0.1,
        "Fed Speak": -0.05,
        "Tech Breakout": +0.2,
        "Geopolitical Risk": -0.15,
        "Strong Earnings": +0.1
    }
    score_adjust = sum(modifiers.get(c, 0.0) for c in contexts)
    return round(score_adjust, 4)