class RecursiveQuantumAgent:
    def __init__(self):
        self.agents = []

    def spawn_quantum_agent(self, agent_name, quantum_factor):
        """Spawn recursive quantum agents that evolve based on quantum states."""
        agent = {"name": agent_name, "quantum_factor": quantum_factor, "state": "active"}
        self.agents.append(agent)
        print(f"Spawned quantum agent: {agent_name} with factor: {quantum_factor}")
    
    def get_agents(self):
        return self.agents