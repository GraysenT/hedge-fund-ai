from agents.agent import AIAgent
from registry.agent_registry import AgentRegistry  # 👈 add this

active_agents = {}

def spawn_agent(name: str, strategy: str = None, memory_enabled=True, goal=None):
    import uuid
    agent_id = str(uuid.uuid4())
    agent = AIAgent(name=name, strategy_name=strategy, memory_enabled=memory_enabled, goal=goal)

    active_agents[agent_id] = agent
    AgentRegistry.register(agent_id, agent)  # 👈 register agent globally

    return agent_id, agent