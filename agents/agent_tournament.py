import json
import os
from collections import defaultdict

AGENT_PATH = "agents/agent_registry.json"
PERF_PATH = "memory/performance"
OUTPUT_PATH = "agents/agent_tournament_results.json"

def load_agent_registry():
    with open(AGENT_PATH) as f:
        return json.load(f)

def load_recent_performance(days=5):
    files = sorted(os.listdir(PERF_PATH))[-days:]
    perf_data = []
    for file in files:
        with open(os.path.join(PERF_PATH, file)) as f:
            perf_data.append(json.load(f))
    return perf_data

def evaluate_agents(agent_map, perf_data):
    agent_scores = defaultdict(lambda: {"pnl": 0, "days": 0, "strategies": []})
    for daily in perf_data:
        for agent, strats in agent_map.items():
            for strat in strats:
                if strat in daily:
                    agent_scores[agent]["pnl"] += daily[strat]["pnl"]
                    agent_scores[agent]["days"] += 1
                    if strat not in agent_scores[agent]["strategies"]:
                        agent_scores[agent]["strategies"].append(strat)
    return agent_scores

def save_results(agent_scores):
    with open(OUTPUT_PATH, "w") as f:
        json.dump(agent_scores, f, indent=2)
    print(f"🏆 Agent tournament results saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    agents = load_agent_registry()
    perf_data = load_recent_performance()
    results = evaluate_agents(agents, perf_data)
    save_results(results)

    print("\n📊 Agent Scores:")
    for agent, stats in results.items():
        print(f"{agent} → ${round(stats['pnl'], 2)} over {stats['days']} days with {len(stats['strategies'])} strategies.")
        