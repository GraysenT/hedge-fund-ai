def adjust_exposure_by_alpha(agents):
    """
    Dynamically adjusts exposure weight per agent based on alpha consistency and drawdown protection.
    """
    for agent in agents:
        signal_quality = agent.get("alpha_quality", 0.5)
        risk_score = agent.get("risk", 0.5)
        agent["exposure_weight"] = min(1.0, max(0.0, signal_quality - risk_score))
    return agents