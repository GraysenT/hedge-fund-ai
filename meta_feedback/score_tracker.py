Below is a Python script that tracks how each module's score changes across time and context. The script uses a dictionary to store scores for different modules over different timestamps and contexts. It provides functionality to add scores, update scores, and retrieve the history of scores for each module.

```python
import datetime

class ModuleScoreTracker:
    def __init__(self):
        # Dictionary to store scores in the format:
        # {module_name: {context: [(timestamp, score), ...]}}
        self.scores = {}

    def add_score(self, module_name, context, score):
        """Add a new score for a module in a specific context."""
        timestamp = datetime.datetime.now()
        if module_name not in self.scores:
            self.scores[module_name] = {}
        if context not in self.scores[module_name]:
            self.scores[module_name][context] = []
        self.scores[module_name][context].append((timestamp, score))

    def update_score(self, module_name, context, new_score):
        """Update the latest score for a module in a specific context."""
        timestamp = datetime.datetime.now()
        if module_name in self.scores and context in self.scores[module_name]:
            self.scores[module_name][context].append((timestamp, new_score))
        else:
            self.add_score(module_name, context, new_score)

    def get_score_history(self, module_name, context):
        """Retrieve the score history for a module in a specific context."""
        if module_name in self.scores and context in self.scores[module_name]:
            return self.scores[module_name][context]
        else:
            return []

# Example usage
if __name__ == "__main__":
    tracker = ModuleScoreTracker()
    tracker.add_score("Module1", "ContextA", 85)
    tracker.add_score("Module1", "ContextB", 90)
    tracker.update_score("Module1", "ContextA", 88)
    tracker.update_score("Module1", "ContextB", 93)

    print("Score History for Module1, ContextA:", tracker.get_score_history("Module1", "ContextA"))
    print("Score History for Module1, ContextB:", tracker.get_score_history("Module1", "ContextB"))
```

This script defines a `ModuleScoreTracker` class that can be used to manage scores for different modules across various contexts and timestamps. The scores are stored in a nested dictionary, and the class provides methods to add, update, and retrieve the score history. The example usage at the bottom demonstrates how to use this class to track scores for a hypothetical module in different contexts.