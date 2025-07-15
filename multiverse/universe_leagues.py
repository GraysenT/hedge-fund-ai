def assign_leagues(worlds):
    leagues = {}
    for name, world in worlds.items():
        total_sharpe = sum(a.sharpe for a in world["agents"])
        if total_sharpe > 50:
            leagues[name] = "S-tier"
        elif total_sharpe > 25:
            leagues[name] = "A-tier"
        else:
            leagues[name] = "B-tier"
    return leagues