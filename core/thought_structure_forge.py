class ThoughtStructureForge:
    def __init__(self):
        self.structure = []

    def build_thought_structure(self, belief, contradiction):
        """Builds strategy, agent, and purpose modules from belief and contradiction."""
        thought = {"belief": belief, "contradiction": contradiction}
        self.structure.append(thought)
        print(f"Thought structure created: {thought}")
    
    def get_thought_structure(self):
        return self.structure