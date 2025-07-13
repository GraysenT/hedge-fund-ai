```python
class StrategicPlanning:
    def __init__(self, beliefs):
        self.beliefs = beliefs
        self.decisions = []

    def add_belief(self, belief):
        self.beliefs.append(belief)

    def make_decision_based_on_beliefs(self):
        decision = "Decisions based on current beliefs: \n"
        for belief in self.beliefs:
            decision += f"- Considering belief: {belief}\n"
            if "growth" in belief:
                decision += "  -> Invest in new markets.\n"
            elif "sustainability" in belief:
                decision += "  -> Implement eco-friendly processes.\n"
            elif "customer focus" in belief:
                decision += "  -> Enhance customer service.\n"
        self.decisions.append(decision)
        return decision

    def get_decisions(self):
        return "\n".join(self.decisions)

# Example usage:
beliefs = ["growth is essential", "sustainability matters", "customer focus is key"]
planning = StrategicPlanning(beliefs)

# Make decisions based on beliefs
decision_output = planning.make_decision_based_on_beliefs()
print(decision_output)

# Retrieve and print all decisions
all_decisions = planning.get_decisions()
print(all_decisions)
```