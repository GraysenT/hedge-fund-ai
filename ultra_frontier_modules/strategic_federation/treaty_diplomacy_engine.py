from .treaty_engine import StrategicTreaty
from .treaty_registry import save_treaty

def propose_strategic_treaty(node_a, node_b, terms):
    treaty = StrategicTreaty(node_a, node_b, terms)
    save_treaty(treaty)
    return treaty