def evolve_cooperative_behavior(agents):
    """
    Identifies cooperative agents and rewards strategies that collaborate effectively.
    """
    for agent in agents:
        if agent.get("cooperation") == "collaborative":
            agent["weight"] += 0.05
            agent["cohesion_score"] = agent.get("cohesion_score", 0.5) + 0.1
    return agents