def evaluate_scenario_path(path):
    """
    Score long-term path favorability using weighted macro-health factors.
    """
    inflation_sum = sum(p["Inflation"] for p in path)
    growth_sum = sum(p["GDP Growth"] for p in path)
    volatility_sum = sum(p["Volatility"] for p in path)

    stability_score = (growth_sum - inflation_sum - volatility_sum * 10) / len(path)
    return round(stability_score, 2)