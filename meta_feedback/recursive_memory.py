```python
class RecursiveThoughts:
    def __init__(self):
        self.history = []
        self.failures = []

    def add_thought(self, thought):
        self.history.append(thought)

    def add_failure(self, failure):
        self.failures.append(failure)

    def get_history(self):
        return self.history

    def get_failures(self):
        return self.failures

# Example usage
if __name__ == "__main__":
    thoughts = RecursiveThoughts()
    thoughts.add_thought("Starting recursion with base case n=1")
    thoughts.add_thought("Recursion step with n=2")
    thoughts.add_failure("Failed at n=3 due to stack overflow")

    print("Thought History:")
    for thought in thoughts.get_history():
        print(thought)

    print("\nFailure Logs:")
    for failure in thoughts.get_failures():
        print(failure)
```