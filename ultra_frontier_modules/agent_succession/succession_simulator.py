from .agent_lineage import SuccessionAgent
from .succession_registry import save_agent

def simulate_succession():
    parent = SuccessionAgent("TrendHunter", role="volatility_reactor")
    child = parent.spawn_child("TrendHunterV2", mutation_notes="optimized for lower beta")

    parent.retire("outperformed by offspring")

    save_agent(parent)
    save_agent(child)

    return {
        "parent": parent.profile(),
        "child": child.profile()
    }

if __name__ == "__main__":
    from pprint import pprint
    pprint(simulate_succession())