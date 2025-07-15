def feedback_loop(agent):
    real_sharpe = agent.sharpe
    dream_sharpe = agent.last_dream_result.get("sharpe", 1)
    delta = real_sharpe - dream_sharpe
    agent.goal_vector["aggression"] += 0.1 * delta
    agent.goal_vector["risk"] -= 0.05 * delta