```python
class EthicalComplianceSystem:
    def __init__(self, alpha_goal_weight, ethical_compliance_weight):
        self.alpha_goal_weight = alpha_goal_weight
        self.ethical_compliance_weight = ethical_compliance_weight

    def evaluate_action(self, action):
        """
        Evaluates an action based on alpha goals and ethical compliance.
        """
        alpha_score = self.evaluate_alpha_goals(action)
        ethical_score = self.evaluate_ethical_compliance(action)

        # Weighted sum of alpha goals and ethical compliance
        total_score = (self.alpha_goal_weight * alpha_score +
                       self.ethical_compliance_weight * ethical_score)
        return total_score

    def evaluate_alpha_goals(self, action):
        """
        Simulates evaluation of alpha goals (e.g., profitability, efficiency).
        """
        # Example: Higher numbers are better
        return action.get("profitability", 0) * 1.5 + action.get("efficiency", 0) * 2

    def evaluate_ethical_compliance(self, action):
        """
        Simulates evaluation of ethical compliance (e.g., fairness, legality).
        """
        # Example: Higher numbers are better
        fairness = action.get("fairness", 0) * 2
        legality = action.get("legality", 0) * 3
        return fairness + legality

# Example usage
system = EthicalComplianceSystem(alpha_goal_weight=0.7, ethical_compliance_weight=0.3)
action = {
    "profitability": 8,
    "efficiency": 7,
    "fairness": 5,
    "legality": 9
}
score = system.evaluate_action(action)
print(f"Total score for the action: {score}")
```