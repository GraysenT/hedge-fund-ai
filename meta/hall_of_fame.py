import json
import os

PERF_PATH = "memory/performance"
AGENT_MEM = "agents/agent_long_term_memory.json"
HOF_FILE = "meta/hall_of_fame.json"

def update_hof():
    hof = {"strategies": {}, "agents": {}}

    # Strategies
    all_perf = [json.load(open(f"memory/performance/{f}")) for f in sorted(os.listdir(PERF_PATH))]
    strat_stats = {}
    for day in all_perf:
        for strat, res in day.items():
            if strat not in strat_stats:
                strat_stats[strat] = 0
            strat_stats[strat] += res["pnl"]

    hof["strategies"] = dict(sorted(strat_stats.items(), key=lambda x: x[1], reverse=True)[:5])

    # Agents
    agents = json.load(open(AGENT_MEM))
    agent_pnls = {k: v["pnl"] for k, v in agents.items()}
    hof["agents"] = dict(sorted(agent_pnls.items(), key=lambda x: x[1], reverse=True)[:5])

    with open(HOF_FILE, "w") as f:
        json.dump(hof, f, indent=2)
    print("🏅 Hall of Fame updated.")

if __name__ == "__main__":
    update_hof()
    