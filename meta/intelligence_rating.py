```python
class IntelligenceScorer:
    def __init__(self, abstraction, complexity, foresight, novelty):
        self.abstraction = abstraction
        self.complexity = complexity
        self.foresight = foresight
        self.novelty = novelty

    def score(self):
        # Weights can be adjusted based on the importance of each factor
        weights = {'abstraction': 0.25, 'complexity': 0.25, 'foresight': 0.25, 'novelty': 0.25}
        total_score = (self.abstraction * weights['abstraction'] +
                       self.complexity * weights['complexity'] +
                       self.foresight * weights['foresight'] +
                       self.novelty * weights['novelty'])
        return total_score

# Example usage:
module_intelligence = IntelligenceScorer(abstraction=8, complexity=7, foresight=9, novelty=6)
print("Intelligence Score:", module_intelligence.score())
```