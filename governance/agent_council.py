Below is a Python simulation of a council of agents with weighted votes to approve major changes. Each agent has a specific weight for their vote, and a proposal passes if the total weight of approving votes exceeds a defined threshold.

```python
class Agent:
    def __init__(self, name, vote_weight):
        self.name = name
        self.vote_weight = vote_weight

    def vote(self, proposal):
        # Simulate a vote (yes/no) based on some internal logic or external input
        # Here, it's randomized for simplicity
        import random
        return random.choice([True, False])

class Council:
    def __init__(self, agents, approval_threshold):
        self.agents = agents
        self.approval_threshold = approval_threshold

    def propose_change(self, proposal):
        total_votes = 0
        yes_votes_weight = 0

        print(f"Proposal: {proposal}")
        for agent in self.agents:
            vote = agent.vote(proposal)
            vote_str = "Yes" if vote else "No"
            print(f"{agent.name} votes {vote_str} with weight {agent.vote_weight}")

            if vote:
                yes_votes_weight += agent.vote_weight

            total_votes += agent.vote_weight

        print(f"Total weighted votes: {total_votes}, Yes votes weight: {yes_votes_weight}")
        
        if yes_votes_weight >= self.approval_threshold:
            print("Proposal Approved")
            return True
        else:
            print("Proposal Rejected")
            return False

# Example usage
agents = [
    Agent("Alice", 10),
    Agent("Bob", 20),
    Agent("Charlie", 30),
    Agent("Diana", 40)
]

# Create a council with a threshold of 51% of the total weight
total_weight = sum(agent.vote_weight for agent in agents)
threshold = total_weight * 0.51

council = Council(agents, threshold)
council.propose_change("Increase budget by 10%")
```

This code defines a simple framework where each agent can vote "yes" or "no" on a proposal, and their votes are weighted. The `Council` class handles the proposal and calculates whether it passes based on the weighted votes. The example usage at the end sets up a council with four agents and a proposal to increase the budget. The threshold for approval is set to 51% of the total vote weight.