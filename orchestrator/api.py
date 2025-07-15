from fastapi import APIRouter
from orchestrator.agent_manager import spawn_agent, active_agents
from signals.logger import log_signal

router = APIRouter()

@router.post("/spawn")
def spawn(name: str, strategy: str = None):
    agent_id, agent = spawn_agent(name, strategy)
    return {"agent_id": agent_id, "name": name, "strategy": strategy}

@router.post("/think/{agent_id}")
def think(agent_id: str, market_data: dict):
    agent = active_agents.get(agent_id)
    if not agent:
        return {"error": "Agent not found"}
    signal = agent.think(market_data)
    log_signal(agent_id, agent.strategy_name, signal, market_data)
    return {"signal": signal}

@router.post("/evolve/{agent_id}")
def evolve(agent_id: str):
    agent = active_agents.get(agent_id)
    if not agent:
        return {"error": "Agent not found"}
    return {"patch": agent.evolve()}

@router.get("/status")
def status():
    return {"agents": list(active_agents.keys())}

@router.get("/status")
def system_status():
    from registry.agent_registry import AgentRegistry
    agents = AgentRegistry.all()
    report = []
    for agent in agents:
        report.append({
            "name": agent.name,
            "sharpe": getattr(agent, "sharpe_score", None),
            "strategy": agent.__class__.__name__,
        })
    return {"agents": report}