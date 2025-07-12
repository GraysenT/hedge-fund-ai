def observe_intelligence_growth(metrics):
    """
    Tracks how logic complexity and strategic diversity evolve over time.
    """
    growth_index = 0
    for m in metrics:
        growth_index += m.get("signal_depth", 0) + m.get("strategy_breadth", 0)
    return growth_index