```python
from collections import deque

class ExperimentQueue:
    def __init__(self):
        self.queue = deque()

    def add_experiment(self, experiment_name, strategy, logic_upgrade):
        self.queue.append({
            "experiment_name": experiment_name,
            "strategy": strategy,
            "logic_upgrade": logic_upgrade
        })

    def get_next_experiment(self):
        if self.queue:
            return self.queue.popleft()
        else:
            return "No more experiments in the queue"

    def view_upcoming_experiments(self):
        return list(self.queue)

# Example usage:
experiment_queue = ExperimentQueue()

# Adding experiments to the queue
experiment_queue.add_experiment("Experiment 1", "Strategy A", "Logic 1.0")
experiment_queue.add_experiment("Experiment 2", "Strategy B", "Logic 2.0")
experiment_queue.add_experiment("Experiment 3", "Strategy C", "Logic 3.0")

# Viewing the upcoming experiments
print("Upcoming Experiments:", experiment_queue.view_upcoming_experiments())

# Getting the next experiment
print("Next Experiment:", experiment_queue.get_next_experiment())

# Viewing the updated list of upcoming experiments
print("Updated Upcoming Experiments:", experiment_queue.view_upcoming_experiments())
```