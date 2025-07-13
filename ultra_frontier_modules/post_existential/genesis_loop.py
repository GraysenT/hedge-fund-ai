from .self_simulator import SelfSimulationInstance
from .conscious_agent_memory import append_to_memory

def run_genesis_cycle(seed="System-AI-Core"):
    agent = SelfSimulationInstance(purpose="Self-Expansion & Continuity", seed_identity=seed)
    agent.simulate()
    result = agent.result()
    append_to_memory(result)
    return result

if __name__ == "__main__":
    from pprint import pprint
    pprint(run_genesis_cycle())