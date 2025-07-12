def reallocate_focus_to_high_signal_agents(agents):
    """
    Boosts cycle frequency and resources to agents generating high-confidence signals.
    """
    for agent in agents:
        if agent.get("confidence", 0.0) > 0.85:
            agent["update_interval"] = max(1, agent.get("update_interval", 5) - 1)
    return agents