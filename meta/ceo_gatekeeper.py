import json
import os
from datetime import datetime, timedelta

FIREWALL = "meta/alpha_firewall.json"
AUDITS = "reporting/audits"

def approve_evolution():
    # Check audit freshness
    recent = sorted(os.listdir(AUDITS))[-1]
    audit_date = datetime.strptime(recent.split("_")[1].split(".")[0], "%Y-%m-%d")
    if datetime.now() - audit_date > timedelta(days=1):
        print("❌ Audit too old. Evolution vetoed.")
        return False

    # Check firewall
    if os.path.exists(FIREWALL):
        blocked = json.load(open(FIREWALL))
        if len(blocked) > 5:
            print("🛑 Too many firewalled strategies.")
            return False

    print("✅ Evolution approved by Meta-CEO.")
    return True

if __name__ == "__main__":
    if approve_evolution():
        import subprocess
        subprocess.call(["python3", "evolve.py"])
        