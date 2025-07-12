def align_strategy_to_historical_epoch(strategy, regime_features):
    """
    Scores strategy alignment with historical economic or behavioral epochs.
    """
    score = 0
    for f in regime_features:
        if f in strategy.get("traits", []):
            score += 1
    return score / len(regime_features)