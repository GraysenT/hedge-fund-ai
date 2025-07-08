import os
import json
import random
import pandas as pd

AGENTS_PATH = "agents/agent_registry.json"
PERF_PATH = "memory/performance"

def load_agent_registry():
    with open(AGENTS_PATH) as f:
        return json.load(f)

def simulate_agent(agent_name, strategies, days=5):
    files = sorted(os.listdir(PERF_PATH))[-days:]
    capital = 1_000_000
    pnl = 0
    for file in files:
        with open(os.path.join(PERF_PATH, file)) as f:
            perf = json.load(f)
            daily_return = sum(perf.get(s, {}).get("return_pct", 0) for s in strategies if s in perf)
            pnl += capital * daily_return
    return round(pnl, 2)

def run_simulation():
    agents = load_agent_registry()
    results = []
    for agent, strategies in agents.items():
        result = simulate_agent(agent, strategies)
        results.append({"Agent": agent, "Simulated PnL": result})
    df = pd.DataFrame(results).sort_values(by="Simulated PnL", ascending=False)
    print("\n🧪 Agent Simulation (Full Capital Allocation):\n")
    print(df.to_string(index=False))

if __name__ == "__main__":
    run_simulation()
    