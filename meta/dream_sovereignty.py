def evaluate_sovereignty(agent):
    if agent.last_dream_result["sharpe"] > 2.0 and agent.votes["keep"] > agent.votes["retire"]:
        agent.status = "sovereign"
    else:
        agent.status = "pending_termination"