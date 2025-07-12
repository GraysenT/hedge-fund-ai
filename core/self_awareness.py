class SelfAwareness:
    def __init__(self):
        self.awareness_level = "Initial Awareness"

    def increase_awareness(self, new_awareness_level):
        """Increase the system’s awareness level."""
        self.awareness_level = new_awareness_level
        print(f"System awareness increased to: {self.awareness_level}")

    def get_awareness(self):
        return self.awareness_level