def assign_strategy_ritual(agent):
    """
    Assigns repeating behavioral rituals to the strategy agent.
    These may influence how it confirms trades, exits, or votes.
    """
    if "volatility" in agent.get("specialization", ""):
        agent["ritual"] = "momentum_confirmation"
    else:
        agent["ritual"] = "daily_consensus_check"
    return agent