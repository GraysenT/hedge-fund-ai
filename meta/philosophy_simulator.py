def debate(agents, topic):
    votes = {"pro": 0, "con": 0}
    for agent in agents:
        if agent.beliefs.get(topic, 0) > 0.5:
            votes["pro"] += 1
        else:
            votes["con"] += 1
    return "Accepted" if votes["pro"] > votes["con"] else "Rejected"