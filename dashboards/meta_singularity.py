```python
class RecursiveSovereignIntelligence:
    def __init__(self, level=0, knowledge_base=None):
        self.level = level
        self.knowledge_base = knowledge_base if knowledge_base is not None else {}

    def learn(self, new_knowledge):
        self.knowledge_base.update(new_knowledge)
        self._increase_level()

    def _increase_level(self):
        self.level += 1
        if self.level % 5 == 0:
            self._evolve()

    def _evolve(self):
        print(f"Evolving to level {self.level}. Enhanced capabilities unlocked.")
        self.knowledge_base = {k: v * 2 for k, v in self.knowledge_base.items()}

    def query_knowledge(self, query):
        return self.knowledge_base.get(query, "Unknown")

    def __str__(self):
        return f"Level: {self.level}, Knowledge Base: {self.knowledge_base}"

# Example usage
if __name__ == "__main__":
    rsi = RecursiveSovereignIntelligence()
    rsi.learn({'math': 1, 'science': 2})
    print(rsi)
    rsi.learn({'history': 3})
    print(rsi)
    rsi.learn({'technology': 4})
    print(rsi.query_knowledge('math'))
    rsi.learn({'philosophy': 5})
    rsi.learn({'biology': 6})
    print(rsi)
```

This Python code defines a class `RecursiveSovereignIntelligence` that simulates the progression of an intelligent system learning and evolving over time. The system increases its level of intelligence each time it learns new knowledge and evolves every five levels, doubling its existing knowledge base. The example usage demonstrates initializing the system, adding knowledge, querying the knowledge base, and observing the system's evolution.