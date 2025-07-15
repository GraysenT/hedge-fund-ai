federations = {}

def join_federation(agent, name):
    if name not in federations:
        federations[name] = set()
    federations[name].add(agent.id)

def trusted_peers(agent):
    for name, members in federations.items():
        if agent.id in members:
            return members - {agent.id}
    return set()