from .morphable_strategy import MorphableStrategy
from .memory_bridge import extract_morph_triggers

def simulate_morphogenesis():
    strategy = MorphableStrategy(
        base_name="AlphaMomentum",
        base_logic={"lookback": 20, "threshold": 1.5, "leverage": 2.0},
        sensitivity=0.6
    )

    mock_memory = [
        {
            "strategy": "AlphaMomentum",
            "outcome": "underperform",
            "context": "HighVol",
            "suggested_fix": {"threshold": -0.2}
        },
        {
            "strategy": "AlphaMomentum",
            "outcome": "underperform",
            "context": "LowTrend",
            "suggested_fix": {"lookback": 5}
        }
    ]

    triggers = extract_morph_triggers(mock_memory, "AlphaMomentum")
    for t in triggers:
        strategy.morph(t)

    return {
        "final_logic": strategy.base_logic,
        "mutation_log": strategy.mutation_history
    }

if __name__ == "__main__":
    from pprint import pprint
    pprint(simulate_morphogenesis())