def encode_strategy_culture(agent):
    """
    Tags each strategy agent with cultural identity traits like origin type, goal preference, and ritual behavior.
    """
    culture = {
        "origin_class": agent.get("class", "unknown"),
        "ritual": agent.get("ritual", "default"),
        "risk_tendency": agent.get("risk_profile", "neutral"),
        "cooperation_mode": agent.get("cooperation", "solo"),
    }
    agent["culture"] = culture
    return agent