def simulate_downstream_consequences(strategy):
    """
    Predicts secondary and tertiary consequences of deploying a given strategy.
    """
    logic = strategy.get("logic", "")
    if "overleveraged entry" in logic or "ignore liquidity" in logic:
        return {"risk": "Cascading loss risk if market turns"}
    return {"risk": "Acceptable under current conditions"}