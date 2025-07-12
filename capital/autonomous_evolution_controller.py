class AutonomousEvolutionController:
    def __init__(self):
        self.evolution_steps = []

    def control_evolution(self, step_name, factor):
        """Control the recursive evolution of the system autonomously."""
        step = {"step_name": step_name, "factor": factor}
        self.evolution_steps.append(step)
        print(f"Controlled evolution step: {step_name} with factor: {factor}")
    
    def get_evolution_steps(self):
        return self.evolution_steps