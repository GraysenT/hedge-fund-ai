import random
import copy

class IdeaGenome:
    def __init__(self, idea: str):
        self.idea = idea
        self.version = 1

    def mutate(self):
        suffixes = [" using AI", " powered by federated nodes", " with recursive agents"]
        new_idea = self.idea + random.choice(suffixes)
        clone = copy.deepcopy(self)
        clone.idea = new_idea
        clone.version += 1
        return clone