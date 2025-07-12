```python
import numpy as np

class AutonomySystem:
    def __init__(self, interactions_matrix):
        """
        Initialize the system with an interactions matrix that defines how different components of the system interact.
        :param interactions_matrix: A square numpy array where each element (i, j) represents the influence of component j on component i.
        """
        self.interactions_matrix = np.array(interactions_matrix)
        self.n_components = self.interactions_matrix.shape[0]

    def calculate_independence(self):
        """
        Calculate the independence of each component based on the interactions matrix.
        Independence is defined as the ratio of the sum of self-interactions to the sum of all interactions for each component.
        """
        total_influences = np.sum(self.interactions_matrix, axis=1)
        self_influences = np.diag(self.interactions_matrix)
        independence_scores = self_influences / total_influences
        return independence_scores

    def calculate_self_reinforcement(self):
        """
        Calculate the self-reinforcement score for the system.
        Self-reinforcement is defined as the trace of the interactions matrix divided by the sum of all interactions.
        """
        total_interactions = np.sum(self.interactions_matrix)
        self_reinforcement_score = np.trace(self.interactions_matrix) / total_interactions
        return self_reinforcement_score

    def system_autonomy_score(self):
        """
        Calculate the overall autonomy score of the system.
        This score is a weighted average of the mean independence and the self-reinforcement score.
        """
        independence_scores = self.calculate_independence()
        mean_independence = np.mean(independence_scores)
        self_reinforcement = self.calculate_self_reinforcement()
        
        # Weights can be adjusted based on the importance of independence vs self-reinforcement
        weight_independence = 0.5
        weight_self_reinforcement = 0.5
        
        autonomy_score = (weight_independence * mean_independence + weight_self_reinforcement * self_reinforcement)
        return autonomy_score

# Example usage:
interactions = [
    [0.8, 0.1, 0.1],
    [0.2, 0.7, 0.1],
    [0.1, 0.2, 0.7]
]

system = AutonomySystem(interactions)
print("Independence Scores:", system.calculate_independence())
print("Self-Reinforcement Score:", system.calculate_self_reinforcement())
print("System Autonomy Score:", system.system_autonomy_score())
```

This Python code defines a class `AutonomySystem` that quantifies the autonomy of a system based on an interactions matrix. The matrix represents how components of a system influence each other, with higher autonomy indicated by higher self-influence and lower external influence. The class provides methods to calculate independence scores for each component, a self-reinforcement score for the system, and an overall autonomy score combining these metrics.