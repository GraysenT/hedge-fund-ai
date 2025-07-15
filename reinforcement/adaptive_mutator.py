import random

def adapt_mutation(config):
    if config.get("momentum") < 0.3:
        config["momentum"] += 0.05
    config["threshold"] *= random.uniform(0.95, 1.05)
    return config