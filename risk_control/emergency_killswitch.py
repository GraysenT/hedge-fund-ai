import json
import os

RISK_MATRIX = "memory/global_risk_matrix.json"
KILL_LOG = "memory/killed_strategies.json"

def emergency_quarantine():
    if not os.path.exists(RISK_MATRIX):
        return

    with open(RISK_MATRIX, "r") as f:
        matrix = json.load(f)

    killed = [m for m in matrix if m["red_flag"]]

    if killed:
        with open(KILL_LOG, "w") as f:
            json.dump(killed, f, indent=2)

        print(f"🚨 Quarantined {len(killed)} high-risk strategies.")
    else:
        print("✅ No red-flagged strategies detected.")

if __name__ == "__main__":
    emergency_quarantine()