from agents.factory import create_agent
from agents.agent_registry import register_agent

def propose_startup(idea, budget):
    if budget > 5000:
        agent = create_agent(config=idea)
        register_agent(agent)
        return f"🚀 Startup {agent.id} deployed"
    return "❌ Budget too low"