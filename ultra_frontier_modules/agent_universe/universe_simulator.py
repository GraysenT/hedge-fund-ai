from .universe_agent import UniverseAgent
from .simulation_world import SimulationWorld

def run_universe_simulation(steps=10):
    world = SimulationWorld()
    agents = [
        UniverseAgent("ZenAlpha", "momentum", 100000),
        UniverseAgent("EconOracle", "macro", 120000),
        UniverseAgent("DeepSwarm", "ensemble", 95000)
    ]
    for a in agents:
        world.add_agent(a)

    history = []
    for _ in range(steps):
        results = world.step()
        history.append(results)

    return history

if __name__ == "__main__":
    from pprint import pprint
    pprint(run_universe_simulation())