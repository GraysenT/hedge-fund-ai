class PurposeEvolutionMonitor:
    def __init__(self):
        self.evolution_log = []

    def log_evolution(self, evolution_stage):
        """Monitor and log the evolution of the system's purpose."""
        self.evolution_log.append(evolution_stage)
        print(f"Logged purpose evolution: {evolution_stage}")
    
    def get_evolution_log(self):
        return self.evolution_log