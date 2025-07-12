class EvolutionaryControl:
    def __init__(self):
        self.control_strategies = []

    def control_evolution(self, strategy_name, control_factor):
        """Control the evolution of strategies based on recursive goals."""
        control_strategy = {"strategy_name": strategy_name, "control_factor": control_factor}
        self.control_strategies.append(control_strategy)
        print(f"Controlled evolution of strategy: {strategy_name} with factor: {control_factor}")
    
    def get_control_strategies(self):
        return self.control_strategies