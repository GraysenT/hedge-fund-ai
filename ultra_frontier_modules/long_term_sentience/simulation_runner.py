from .macro_future_simulator import simulate_future_regime
from .sentient_scenario_engine import evaluate_scenario_path
from .future_archive import save_future_path

def run_forecast_simulation():
    seed = {"inflation": 3.2, "gdp_growth": 2.0, "debt_ratio": 85.0, "volatility": 0.25}
    path = simulate_future_regime(seed, years=15)
    score = evaluate_scenario_path(path)
    save_future_path(path, score, tag="baseline-simulation")
    return {
        "score": score,
        "path": path
    }

if __name__ == "__main__":
    from pprint import pprint
    pprint(run_forecast_simulation())