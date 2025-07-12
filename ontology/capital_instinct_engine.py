def encode_instinct(agent):
    """
    Installs risk survival logic and long-term reward orientation into the agent's operating loop.
    """
    agent["instincts"] = {
        "avoid_max_drawdown": True,
        "seek_consistency_over_spikes": True,
        "respect_belief_integrity": True
    }
    return agent