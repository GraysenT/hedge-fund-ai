def vote_on_fork(agents):
    top_agents = sorted(agents, key=lambda x: x.sharpe, reverse=True)[:3]
    return [a.id for a in top_agents if a.sharpe > 2.0]