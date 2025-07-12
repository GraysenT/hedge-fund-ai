def evaluate_capital_mindfulness(agent):
    """
    Measures how well a strategy respects capital rules, liquidity, and systemic coherence.
    """
    max_risk = agent.get("max_risk", 0.1)
    usage = agent.get("exposure_weight", 0.05)
    mindfulness_score = max(0.0, 1 - abs(usage - max_risk) * 10)
    agent["mindfulness_score"] = mindfulness_score
    return agent