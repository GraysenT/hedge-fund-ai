class AgentRegistry:
    _agents = {}

    @classmethod
    def register(cls, agent_id, agent_instance):
        cls._agents[agent_id] = agent_instance

    @classmethod
    def get(cls, agent_id):
        return cls._agents.get(agent_id)

    @classmethod
    def all(cls):
        return cls._agents.values()

    @classmethod
    def get_top_agents(cls, metric="sharpe", threshold=0.2):
        # Simulated: attach `sharpe_score` to each agent during backtesting
        return [
            agent for agent in cls._agents.values()
            if hasattr(agent, "sharpe_score") and agent.sharpe_score > threshold
        ]