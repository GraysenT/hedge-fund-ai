import copy
import random

def crossover_strategies(config_a, config_b):
    """
    Merges two configs into a new child strategy config.
    """
    child = {}
    for key in config_a:
        if key in config_b:
            child[key] = random.choice([config_a[key], config_b[key]])
        else:
            child[key] = config_a[key]
    return child

def mutate_config(config, mutation_rate=0.1):
    mutated = copy.deepcopy(config)
    for key in mutated:
        if isinstance(mutated[key], (int, float)) and random.random() < mutation_rate:
            mutated[key] *= random.uniform(0.8, 1.2)
    return mutated