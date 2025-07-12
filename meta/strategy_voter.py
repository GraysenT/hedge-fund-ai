Below is a Python implementation of a democratic voting mechanism for agents to approve logic promotions. This example uses a simple voting system where agents can vote "yes" or "no" on a proposed logic change. The change is approved if it receives a majority of "yes" votes.

```python
class VotingSystem:
    def __init__(self):
        self.votes = []
        self.agents = []

    def register_agent(self, agent_id):
        if agent_id not in self.agents:
            self.agents.append(agent_id)
            print(f"Agent {agent_id} registered successfully.")
        else:
            print(f"Agent {agent_id} is already registered.")

    def cast_vote(self, agent_id, vote):
        if agent_id not in self.agents:
            print(f"Agent {agent_id} is not registered and cannot vote.")
            return

        if vote not in ['yes', 'no']:
            print("Invalid vote. Please vote 'yes' or 'no'.")
            return

        self.votes.append((agent_id, vote))
        print(f"Agent {agent_id} voted {vote}.")

    def count_votes(self):
        yes_count = sum(1 for _, vote in self.votes if vote == 'yes')
        no_count = sum(1 for _, vote in self.votes if vote == 'no')

        print(f"Total votes: {len(self.votes)} - Yes: {yes_count}, No: {no_count}")
        if yes_count > no_count:
            print("The motion is approved.")
        elif yes_count < no_count:
            print("The motion is rejected.")
        else:
            print("The vote is tied. The motion is not approved.")

    def reset_votes(self):
        self.votes = []
        print("Votes have been reset.")

# Example usage
voting_system = VotingSystem()
voting_system.register_agent('agent1')
voting_system.register_agent('agent2')
voting_system.register_agent('agent3')

voting_system.cast_vote('agent1', 'yes')
voting_system.cast_vote('agent2', 'no')
voting_system.cast_vote('agent3', 'yes')

voting_system.count_votes()  # This will count and display the result of the votes
```

This code defines a `VotingSystem` class that allows agents to register, cast votes, count votes, and reset votes. The voting results are determined by a simple majority rule. The example usage shows how to use the class to conduct a vote among three agents.