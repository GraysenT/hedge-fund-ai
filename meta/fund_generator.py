import uuid
import os
import json
import random

FUND_TEMPLATE = {
    "AlphaPulse": ["momentum", "macro"],
    "StatUniverse": ["stat_arb", "mean_reversion"],
    "ThetaHawk": ["options_flow", "volatility"],
    "QuantumSpot": ["crypto", "fx", "anomaly"]
}

def create_virtual_funds():
    os.makedirs("memory/funds_generated", exist_ok=True)
    for name, tags in FUND_TEMPLATE.items():
        fund_id = f"{name}_{uuid.uuid4().hex[:4]}"
        strat_list = [{
            "strategy": f"{tag}_{uuid.uuid4().hex[:3]}",
            "weight": round(random.uniform(0.01, 0.3), 4)
        } for tag in tags]
        with open(f"memory/funds_generated/{fund_id}.json", "w") as f:
            json.dump(strat_list, f, indent=2)
        print(f"🧬 New virtual fund created: {fund_id} with {len(strat_list)} strategies")

if __name__ == "__main__":
    create_virtual_funds()