import random

def recombine_strategies(strat_a, strat_b):
    """
    Mix parameters between two strategy configurations.
    """
    new_strat = {}
    for key in strat_a:
        if key in strat_b:
            new_strat[key] = random.choice([strat_a[key], strat_b[key]])
    return new_strat

def mutate_strategy(strat, rate=0.1):
    """
    Randomly mutate numeric parameters slightly.
    """
    for key in strat:
        if isinstance(strat[key], (int, float)) and random.random() < rate:
            strat[key] *= random.uniform(0.9, 1.1)
    return strat