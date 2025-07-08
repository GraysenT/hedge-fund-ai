import json
import os

LINEAGE = "strategy_memory/strategy_lineage.json"
PERF_PATH = "memory/performance"
VETO_LIST = "meta/alpha_firewall.json"

def firewall_check():
    perf = json.load(open(f"memory/performance/{sorted(os.listdir(PERF_PATH))[-1]}"))
    lineage = json.load(open(LINEAGE))
    veto = []

    for strat, res in perf.items():
        if res["return_pct"] < -0.1 and lineage.get(strat, {}).get("depth", 0) > 3:
            veto.append(strat)

    json.dump(veto, open(VETO_LIST, "w"), indent=2)
    print("🚫 Alpha firewall engaged.")
    for v in veto:
        print(f"❌ Blocked: {v}")

def is_firewalled(strat):
    if not os.path.exists(VETO_LIST):
        return False
    return strat in json.load(open(VETO_LIST))

if __name__ == "__main__":
    firewall_check()
    