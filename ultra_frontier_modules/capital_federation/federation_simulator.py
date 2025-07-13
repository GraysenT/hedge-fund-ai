from .federated_agent import FederatedAgent
from .federation_controller import CapitalFederation

def run_federation_demo():
    federation = CapitalFederation()

    # Create agents
    agents = [
        FederatedAgent("Momentum", 1_000_000, "momentum", 0.6),
        FederatedAgent("MacroSentient", 1_200_000, "macro", 0.7),
        FederatedAgent("SignalSwarm", 900_000, "ensemble", 0.8)
    ]
    for a in agents:
        federation.register_agent(a)

    # Simulate proposal
    proposal_id = "P001"
    federation.propose_allocation(proposal_id, "Deploy $150k to Volatility Strategy", 150_000)
    federation.broadcast_vote_request(proposal_id)
    result = federation.resolve_proposal(proposal_id)

    return result

if __name__ == "__main__":
    from pprint import pprint
    pprint(run_federation_demo())