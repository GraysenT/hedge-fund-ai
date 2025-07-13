from .context_belief import ContextBelief
from .belief_mesh import BeliefMesh

def simulate_belief_mesh():
    mesh = BeliefMesh()

    b1 = ContextBelief("FedHawkish", "The Fed will maintain higher-for-longer", 0.8)
    b2 = ContextBelief("AI Alpha", "AI-related strategies will continue outperforming", 0.9)
    b3 = ContextBelief("LiquidityCrunch", "Global liquidity conditions are deteriorating", 0.6)

    for b in [b1, b2, b3]:
        mesh.register_belief(b)

    mesh.update_belief("LiquidityCrunch", 0.72)
    entropy = mesh.compute_mesh_entropy()
    beliefs = mesh.export_mesh()

    return {
        "entropy": entropy,
        "mesh": beliefs
    }

if __name__ == "__main__":
    from pprint import pprint
    pprint(simulate_belief_mesh())