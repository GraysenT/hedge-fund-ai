Below is a Python code example that implements a self-reflection tool for agents, allowing them to recursively evaluate their thoughts and score them based on predefined criteria. This example uses a simple class structure to represent an agent and includes methods for thought generation, reflection, and scoring.

```python
class Agent:
    def __init__(self, name):
        self.name = name
        self.thoughts = []
        self.scores = []

    def generate_thought(self):
        # Simulate thought generation (this could be more complex in a real scenario)
        import random
        thoughts_pool = [
            "I need to improve my learning algorithms.",
            "I should analyze more data for better accuracy.",
            "I must ensure my responses are helpful.",
            "I wonder how I can reduce processing time.",
            "I should consider more edge cases in my logic."
        ]
        thought = random.choice(thoughts_pool)
        self.thoughts.append(thought)
        return thought

    def reflect_on_thought(self, thought):
        # Recursive reflection (simplified for this example)
        if len(self.thoughts) < 5:
            new_thought = self.generate_thought()
            return self.reflect_on_thought(new_thought)
        else:
            return self.thoughts

    def score_thoughts(self):
        # Scoring each thought based on arbitrary criteria
        for thought in self.thoughts:
            if "improve" in thought or "better" in thought:
                score = 10
            elif "ensure" in thought or "helpful" in thought:
                score = 8
            elif "reduce" in thought:
                score = 7
            else:
                score = 5
            self.scores.append(score)
        return self.scores

    def self_reflect_and_score(self):
        initial_thought = self.generate_thought()
        self.reflect_on_thought(initial_thought)
        scores = self.score_thoughts()
        return scores

# Example usage:
agent = Agent("AI-1")
scores = agent.self_reflect_and_score()
print(f"Agent {agent.name} generated thoughts: {agent.thoughts}")
print(f"Scores for each thought: {scores}")
```

This code defines an `Agent` class with methods to generate thoughts, reflect on them recursively, and score them. The `self_reflect_and_score` method ties these functionalities together, allowing the agent to perform a complete self-reflection cycle. The scoring system is simplistic and should be adapted to fit specific criteria relevant to the agent's operational context.