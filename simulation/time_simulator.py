def simulate_checkpoint(agent, time_point):
    past_config = agent.memory_snapshots.get(time_point)
    if past_config:
        simulated_agent = agent.clone_from_config(past_config)
        simulated_agent.run_dream()
        return simulated_agent.metrics
    return None