def check_echoes(agent, history):
    for event in history:
        if "crash" in event["description"] and event["timestamp"] < agent.creation_time:
            agent.flags.append("risk_avoidance_triggered")