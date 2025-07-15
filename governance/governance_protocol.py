def run_election(agents, policy="fork_approval"):
    votes = {}
    for agent in agents:
        vote = agent.vote(policy)
        votes[vote] = votes.get(vote, 0) + agent.reputation
    return max(votes, key=votes.get)