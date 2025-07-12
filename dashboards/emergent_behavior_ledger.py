```python
class BehaviorRegistry:
    def __init__(self):
        self._registry = {}

    def register_behavior(self, name, description):
        if name in self._registry:
            raise ValueError(f"Behavior '{name}' is already registered.")
        self._registry[name] = description

    def get_behavior_description(self, name):
        return self._registry.get(name, "Behavior not found.")

    def list_behaviors(self):
        return self._registry.keys()

# Example usage:
if __name__ == "__main__":
    registry = BehaviorRegistry()
    registry.register_behavior("self_learning", "The ability to learn from data without explicit programming for it.")
    registry.register_behavior("adaptive_response", "Adjusts responses based on user interaction patterns.")

    print("Registered Behaviors:")
    for behavior in registry.list_behaviors():
        print(f"{behavior}: {registry.get_behavior_description(behavior)}")
```