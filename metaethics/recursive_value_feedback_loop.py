def update_value_alignment(strategy, feedback):
    """
    Adjusts strategy value score based on post-trade outcome and behavior review.
    """
    score = strategy.get("value_score", 0.5)
    if feedback.get("violated_value"):
        score -= 0.2
    elif feedback.get("reinforced_value"):
        score += 0.2
    strategy["value_score"] = max(0.0, min(1.0, score))
    return strategy