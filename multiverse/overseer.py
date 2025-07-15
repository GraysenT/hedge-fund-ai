def world_stats():
    return {
        name: {
            "agent_count": len(world["agents"]),
            "collapse_risk": 1 - sum(a.sharpe for a in world["agents"]) / 100
        }
        for name, world in worlds.items()
    }