def dream_futures(agent):
    futures = []
    for delta in [-0.1, 0, 0.1]:
        agent.config["risk"] *= 1 + delta
        futures.append(agent.dream_simulation())
    return futures