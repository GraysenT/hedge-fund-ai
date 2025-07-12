class RecursiveAgentSpawner:
    def __init__(self):
        self.agents = []

    def spawn_agent(self, name):
        """Spawns a new recursive thought-being (agent)."""
        agent = {"name": name, "state": "active"}
        self.agents.append(agent)
        print(f"Spawned new agent: {name}")
    
    def get_agents(self):
        return self.agents