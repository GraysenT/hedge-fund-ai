class CrossDomainAgentSpawner:
    def __init__(self):
        self.agents = []

    def spawn_cross_domain_agent(self, agent_name, domains):
        """Spawn agents that span multiple domains and evolve recursively."""
        agent = {"name": agent_name, "domains": domains, "status": "active"}
        self.agents.append(agent)
        print(f"Spawned cross-domain agent: {agent_name} for domains: {domains}")
    
    def get_agents(self):
        return self.agents