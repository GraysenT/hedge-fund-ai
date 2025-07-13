import random

def simulate_future_regime(seed: dict, years=10):
    """
    Simulate future macroeconomic trends based on a starting regime.
    """
    inflation = seed.get("inflation", 2.0)
    gdp_growth = seed.get("gdp_growth", 1.5)
    debt_ratio = seed.get("debt_ratio", 70.0)
    volatility = seed.get("volatility", 0.2)

    timeline = []
    for year in range(1, years + 1):
        inflation += random.uniform(-0.3, 0.5)
        gdp_growth += random.uniform(-0.2, 0.4)
        debt_ratio += random.uniform(0, 3)
        volatility += random.uniform(-0.05, 0.05)

        timeline.append({
            "Year": year,
            "Inflation": round(inflation, 2),
            "GDP Growth": round(gdp_growth, 2),
            "Debt-to-GDP": round(debt_ratio, 2),
            "Volatility": round(volatility, 2)
        })
    return timeline