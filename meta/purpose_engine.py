Below is a Python code example that defines a simple framework for encoding purpose logic to manage long-term goals, directional alignment, and goal tracking. This example uses classes to encapsulate the logic related to goals and their tracking.

```python
class Goal:
    def __init__(self, name, description, target, current=0):
        self.name = name
        self.description = description
        self.target = target
        self.current = current

    def update_progress(self, increment):
        self.current += increment
        self.check_completion()

    def check_completion(self):
        if self.current >= self.target:
            print(f"Goal '{self.name}' completed!")
            return True
        return False

    def status(self):
        return f"{self.name}: {self.current}/{self.target} ({(self.current/self.target)*100:.2f}%)"

class GoalTracker:
    def __init__(self):
        self.goals = []

    def add_goal(self, goal):
        self.goals.append(goal)

    def update_goal(self, goal_name, increment):
        for goal in self.goals:
            if goal.name == goal_name:
                goal.update_progress(increment)
                break

    def check_goals(self):
        for goal in self.goals:
            if goal.check_completion():
                print(f"Goal '{goal.name}' is complete.")
            else:
                print(goal.status())

    def overall_status(self):
        completed = sum(1 for goal in self.goals if goal.current >= goal.target)
        total = len(self.goals)
        print(f"Overall progress: {completed}/{total} goals completed.")

# Example usage
if __name__ == "__main__":
    tracker = GoalTracker()
    tracker.add_goal(Goal("Learn Python", "Complete an advanced Python course", 100))
    tracker.add_goal(Goal("Write a Book", "Finish writing a novel", 300, 10))

    tracker.update_goal("Learn Python", 20)
    tracker.update_goal("Write a Book", 50)
    tracker.check_goals()
    tracker.overall_status()
```

This code defines two classes, `Goal` and `GoalTracker`. The `Goal` class encapsulates the properties of a goal, including its name, description, target value, and current progress. It provides methods to update progress, check if the goal is completed, and get the current status of the goal.

The `GoalTracker` class manages multiple goals. It can add new goals, update the progress of existing goals, check the status of all goals, and provide an overall status of goal completion.

The example usage at the bottom demonstrates how to create a `GoalTracker`, add goals, update their progress, and print their statuses. This framework can be expanded with more features like persistence, different types of goals, and more complex progress evaluations.