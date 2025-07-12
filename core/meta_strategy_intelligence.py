class MetaStrategyIntelligence:
    def __init__(self):
        self.meta_strategies = []

    def create_meta_strategy(self, strategy_name, goal):
        """Create a meta-strategy that optimizes for recursive goals."""
        strategy = {"name": strategy_name, "goal": goal, "status": "active"}
        self.meta_strategies.append(strategy)
        print(f"Created meta-strategy: {strategy_name} with goal: {goal}")
    
    def get_meta_strategies(self):
        return self.meta_strategies