def track_goal_inheritance(agent_history):
    """
    Tracks whether goals set by previous generations of strategies are still active or degraded.
    """
    active_goals = {}
    for agent in agent_history:
        for goal in agent.get("goals", []):
            if goal not in active_goals:
                active_goals[goal] = 0
            active_goals[goal] += 1
    return active_goals