import json
import os
import random

AGENT_PATH = "agents/agent_registry.json"
PERF_PATH = "memory/performance"

with open(AGENT_PATH) as f:
    agents = json.load(f)

files = sorted(os.listdir(PERF_PATH))[-10:]
battle_log = []

agent_names = list(agents.keys())

for i in range(len(agent_names)):
    for j in range(i + 1, len(agent_names)):
        a1, a2 = agent_names[i], agent_names[j]
        pnl1, pnl2 = 0, 0

        for f in files:
            with open(os.path.join(PERF_PATH, f)) as fp:
                daily = json.load(fp)
                pnl1 += sum(daily.get(s, {}).get("pnl", 0) for s in agents[a1])
                pnl2 += sum(daily.get(s, {}).get("pnl", 0) for s in agents[a2])

        winner = a1 if pnl1 > pnl2 else a2
        battle_log.append({"agent_1": a1, "agent_2": a2, "winner": winner})

print("🤺 Agent Battle Results:\n")
for match in battle_log:
    print(f"{match['agent_1']} 🆚 {match['agent_2']} → 🏆 {match['winner']}")
