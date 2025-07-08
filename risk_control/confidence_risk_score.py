import json
import os
import random

DEPLOY_DB = "memory/deployability_scores.json"
CONF_RISK_DB = "memory/confidence_vs_risk.json"

def score_confidence_vs_risk():
    if not os.path.exists(DEPLOY_DB):
        print("❌ No deployability data.")
        return

    with open(DEPLOY_DB, "r") as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"❌ Failed to load JSON: {e}")
            return

    results = []
    for strat in data:
        if "deployability" not in strat:
            print(f"⚠️ Skipping invalid entry: {strat}")
            continue

        confidence = round(strat["deployability"], 2)
        risk = round(random.uniform(0.2, 1.0), 2)
        signal_strength = round(confidence - 0.5 * risk, 3)

        results.append({
            "idea": strat.get("idea", "Unnamed"),
            "confidence": confidence,
            "risk": risk,
            "signal_strength": signal_strength
        })

    with open(CONF_RISK_DB, "w") as f:
        json.dump(results, f, indent=2)

    print(f"📊 Scored {len(results)} strategies for confidence vs risk.")

if __name__ == "__main__":
    score_confidence_vs_risk()