class RecursivePerception:
    def __init__(self):
        self.perception_levels = []

    def adjust_perception(self, level):
        """Adjust the system's perception across recursive layers."""
        self.perception_levels.append(level)
        print(f"Adjusted perception to level: {level}")
    
    def get_perception_levels(self):
        return self.perception_levels