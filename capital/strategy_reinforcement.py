class StrategyReinforcement:
    def __init__(self):
        self.strategies = []

    def reinforce_strategy(self, strategy_name, reinforcement_factor):
        """Reinforce high-performing strategies for long-term success."""
        reinforced_strategy = {"name": strategy_name, "reinforcement_factor": reinforcement_factor}
        self.strategies.append(reinforced_strategy)
        print(f"Reinforced strategy: {strategy_name} with factor: {reinforcement_factor}")
    
    def get_reinforced_strategies(self):
        return self.strategies