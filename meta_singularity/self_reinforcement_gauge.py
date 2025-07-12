```python
class IdeaReinforcementSystem:
    def __init__(self):
        self.ideas = {}
        self.reinforcements = {}

    def add_idea(self, idea_id, idea_content):
        self.ideas[idea_id] = idea_content
        self.reinforcements[idea_id] = 0

    def reinforce_idea(self, idea_id):
        if idea_id in self.reinforcements:
            self.reinforcements[idea_id] += 1
        else:
            print(f"Idea ID {idea_id} not found.")

    def get_reinforcement_count(self, idea_id):
        return self.reinforcements.get(idea_id, 0)

    def reinforcement_success_rate(self):
        total_ideas = len(self.ideas)
        if total_ideas == 0:
            return 0
        total_reinforcements = sum(self.reinforcements.values())
        return total_reinforcements / total_ideas

# Example usage
system = IdeaReinforcementSystem()
system.add_idea(1, "Implement AI model")
system.add_idea(2, "Upgrade server hardware")
system.reinforce_idea(1)
system.reinforce_idea(1)
system.reinforce_idea(2)

print("Reinforcement count for Idea 1:", system.get_reinforcement_count(1))
print("Reinforcement count for Idea 2:", system.get_reinforcement_count(2))
print("Overall reinforcement success rate:", system.reinforcement_success_rate())
```