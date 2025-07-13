from .symbolic_valuation_model import evaluate_symbolic_value

def simulate_value_creation(assets):
    """
    Simulate how shared beliefs increase or decrease perceived value of symbolic assets.
    """
    results = []
    for asset in assets:
        score = evaluate_symbolic_value(asset)
        if score > 0.7:
            outcome = "Spiritual Boom"
        elif score < 0.3:
            outcome = "Myth Collapse"
        else:
            outcome = "Symbolic Drift"
        results.append({
            "Asset": asset.get("name"),
            "Symbolic Score": score,
            "Outcome": outcome
        })
    return results