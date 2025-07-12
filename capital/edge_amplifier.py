def amplify_confident_edges(agents):
    """
    Boosts capital toward strategies with sustained confidence and signal reinforcement.
    """
    for agent in agents:
        confidence = agent.get("confidence", 0.5)
        reinforcement = agent.get("reinforcement_score", 0.5)
        if confidence > 0.7 and reinforcement > 0.6:
            agent["exposure_weight"] *= 1.2
    return agents