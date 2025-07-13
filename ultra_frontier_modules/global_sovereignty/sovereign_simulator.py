from .sovereign_node import SovereignNode
from .zone_command_map import get_zone_agents
from .policy_registry import save_policy

def simulate_sovereign_logic():
    node = SovereignNode("AtlasNode", "Global", authority_level=0.9)
    agents = get_zone_agents("Global")
    decision = f"Deploy agents {agents} to monitor volatility clusters"
    node.log_decision(decision)

    save_policy({
        "node": node.name,
        "decision": node.last_decision,
        "jurisdiction": node.jurisdiction
    })

    return node.last_decision

if __name__ == "__main__":
    from pprint import pprint
    pprint(simulate_sovereign_logic())