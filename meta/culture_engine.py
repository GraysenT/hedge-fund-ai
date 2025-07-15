import random

def evolve_culture(agent):
    traits = agent.culture_vector
    for k in traits:
        traits[k] += random.uniform(-0.05, 0.05)
        traits[k] = max(0, min(1, traits[k]))
    return traits