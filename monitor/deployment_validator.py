import os
import json

MODULES = [
    "memory/deployability_scores.json",
    "memory/confidence_vs_risk.json",
    "memory/optimized_allocations.json",
    "memory/alpha_attribution.json",
    "memory/global_risk_matrix.json",
    "logs/trade_history.json"
]

def validate_deployment():
    status = []
    for path in MODULES:
        exists = os.path.exists(path)
        readable = False
        if exists:
            try:
                with open(path, "r") as f:
                    json.load(f)
                    readable = True
            except:
                readable = False
        status.append({
            "module": path,
            "exists": exists,
            "readable": readable
        })

    healthy = all(s["exists"] and s["readable"] for s in status)
    print("✅ Deployment Validation Result:")
    for s in status:
        symbol = "✅" if s["exists"] and s["readable"] else "❌"
        print(f"{symbol} {s['module']}")

    if healthy:
        print("\n🚀 All systems GO for live deployment.")
    else:
        print("\n🛑 Some systems are broken or missing. Lock deployment until fixed.")

    return healthy

if __name__ == "__main__":
    validate_deployment()