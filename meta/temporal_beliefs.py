def evolve_beliefs(agent):
    current = agent.beliefs
    agent.temporal_beliefs = {
        "past": current.copy(),
        "present": current,
        "future": {k: v * 1.05 for k, v in current.items()}
    }