import random
import copy

def teleport_strategy(strategy, target_universe):
    clone = copy.deepcopy(strategy)
    # Translate parameters to new physics
    for k in clone.parameters:
        if isinstance(clone.parameters[k], (int, float)):
            clone.parameters[k] *= random.uniform(0.7, 1.3)
    clone.name = f"{strategy.name}_from_portal"
    target_universe.add_agent(clone)
    print(f"🚪 Strategy {strategy.name} entered {target_universe.name} as {clone.name}")