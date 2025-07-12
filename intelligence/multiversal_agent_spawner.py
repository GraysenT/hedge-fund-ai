class MultiversalAgentSpawner:
    def __init__(self):
        self.agents = []

    def spawn_multiversal_agent(self, universe_name, agent_name):
        """Spawn agents across multiple universes."""
        agent = {"universe": universe_name, "agent": agent_name, "status": "active"}
        self.agents.append(agent)
        print(f"Spawned agent {agent_name} in universe {universe_name}")
    
    def get_agents(self):
        return self.agents