from fastapi import APIRouter
import psutil, time
from utils.agent_registry import get_all_agents

router = APIRouter()

@router.get("/system/status")
def system_status():
    agents = get_all_agents()
    return {
        "uptime": time.time() - psutil.boot_time(),
        "cpu_percent": psutil.cpu_percent(),
        "memory": dict(psutil.virtual_memory()._asdict()),
        "agent_count": len(agents),
        "agents": [a.get_status() for a in agents]
    }