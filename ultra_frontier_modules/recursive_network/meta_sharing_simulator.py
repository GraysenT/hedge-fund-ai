from .meta_memory_node import MetaMemoryNode
from .network_linker import RecursiveNetwork

def simulate_network_cycle():
    net = RecursiveNetwork()
    n1 = MetaMemoryNode("VisionAI")
    n2 = MetaMemoryNode("SignalCluster")
    n3 = MetaMemoryNode("NarrativeCore")

    for n in [n1, n2, n3]:
        net.add_node(n)

    insight = {
        "topic": "volatility_shift",
        "confidence": 0.78,
        "source": "VisionAI",
        "signal_type": "regime_change"
    }

    n1.receive_insight(insight)
    net.broadcast_insight(n1, insight)
    net.sync_beliefs()

    return [n.export_state() for n in net.nodes]

if __name__ == "__main__":
    from pprint import pprint
    pprint(simulate_network_cycle())