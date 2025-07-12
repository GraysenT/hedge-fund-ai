Below is a Python script that simulates tracking and indexing logic promotions over time with attributes such as score, cycle, and agent. This script uses a simple data structure to store the information and provides functionality to add and retrieve the data.

```python
class LogicPromotion:
    def __init__(self):
        self.promotions = []

    def add_promotion(self, score, cycle, agent):
        """
        Adds a new logic promotion record.
        :param score: int - The score associated with the logic.
        :param cycle: int - The cycle number when the promotion occurred.
        :param agent: str - The name of the agent responsible for the promotion.
        """
        self.promotions.append({
            'score': score,
            'cycle': cycle,
            'agent': agent
        })

    def get_all_promotions(self):
        """
        Returns all promotions.
        :return: list of dicts - Each dict contains score, cycle, and agent.
        """
        return self.promotions

    def get_promotions_by_agent(self, agent_name):
        """
        Retrieves all promotions handled by a specific agent.
        :param agent_name: str - The name of the agent.
        :return: list of dicts - Each dict contains score, cycle, and agent for the specified agent.
        """
        return [promo for promo in self.promotions if promo['agent'] == agent_name]

    def get_promotions_by_cycle(self, cycle_number):
        """
        Retrieves all promotions that occurred in a specific cycle.
        :param cycle_number: int - The cycle number.
        :return: list of dicts - Each dict contains score, cycle, and agent for the specified cycle.
        """
        return [promo for promo in self.promotions if promo['cycle'] == cycle_number]

# Example usage
if __name__ == "__main__":
    logic_promotion_tracker = LogicPromotion()

    # Adding some promotions
    logic_promotion_tracker.add_promotion(score=85, cycle=1, agent="AgentA")
    logic_promotion_tracker.add_promotion(score=90, cycle=2, agent="AgentB")
    logic_promotion_tracker.add_promotion(score=88, cycle=1, agent="AgentC")
    logic_promotion_tracker.add_promotion(score=92, cycle=3, agent="AgentA")

    # Retrieve all promotions
    all_promotions = logic_promotion_tracker.get_all_promotions()
    print("All Promotions:", all_promotions)

    # Retrieve promotions by specific agent
    agent_a_promotions = logic_promotion_tracker.get_promotions_by_agent("AgentA")
    print("Promotions by AgentA:", agent_a_promotions)

    # Retrieve promotions by specific cycle
    cycle_1_promotions = logic_promotion_tracker.get_promotions_by_cycle(1)
    print("Promotions in Cycle 1:", cycle_1_promotions)
```

This script defines a `LogicPromotion` class to manage the logic promotions. It allows adding new promotions and retrieving promotions either by all records, by a specific agent, or by a specific cycle. The example usage demonstrates how to use this class to manage and query the data.