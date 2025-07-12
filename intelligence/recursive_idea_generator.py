import random

class RecursiveIdeaGenerator:
    def __init__(self):
        self.ideas = []

    def generate_idea(self):
        """Generates a recursive idea based on the system's current state."""
        idea = f"Recursive Idea #{random.randint(1, 1000)}"
        self.ideas.append(idea)
        print(f"Generated idea: {idea}")
    
    def get_ideas(self):
        return self.ideas