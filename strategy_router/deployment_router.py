import json
import os

DEPLOY_DB = "memory/deployability_scores.json"
THRESHOLD = 0.65

def apply_deployability_filters():
    if not os.path.exists(DEPLOY_DB):
        print("⚠️ No deployability data.")
        return

    with open(DEPLOY_DB, "r") as f:
        scores = json.load(f)

    approved = []
    for s in scores:
        if "deployability" in s and s["deployability"] >= THRESHOLD:
            approved.append(s)

    with open("memory/deployment_approved.json", "w") as f:
        json.dump(approved, f, indent=2)

    print(f"✅ Approved {len(approved)} strategies for deployment.")