```python
class SimulationFeedback:
    def __init__(self):
        self.feedback_storage = []

    def add_feedback(self, simulation_data, label):
        """
        Stores feedback along with its corresponding label.

        Args:
        simulation_data (dict): The data generated from the simulation.
        label (str): The judgment label for the simulation data.
        """
        self.feedback_storage.append((simulation_data, label))

    def get_all_feedback(self):
        """
        Returns all stored feedback and labels.

        Returns:
        list of tuples: List containing tuples of simulation data and labels.
        """
        return self.feedback_storage

# Example usage:
sim_feedback = SimulationFeedback()
sim_feedback.add_feedback({'temperature': 22, 'pressure': 101.3}, 'normal')
sim_feedback.add_feedback({'temperature': 30, 'pressure': 110.5}, 'high')

all_feedback = sim_feedback.get_all_feedback()
print(all_feedback)
```