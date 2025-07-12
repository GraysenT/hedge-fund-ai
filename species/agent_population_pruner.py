def prune_inactive_agents(agents, threshold=0.01):
    """
    Removes agents with low performance and long inactivity.
    """
    return [a for a in agents if a.get("activity", 0) > threshold or a.get("score", 0) > 0.0]