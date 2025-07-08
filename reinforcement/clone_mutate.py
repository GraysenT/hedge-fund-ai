import json
import os
from datetime import datetime
import random

LINEAGE_PATH = "strategy_memory/strategy_lineage.json"
PERF_PATH = "memory/performance"

# Load latest performance
latest_perf = sorted(os.listdir(PERF_PATH))[-1]
with open(os.path.join(PERF_PATH, latest_perf)) as f:
    perf = json.load(f)

# Pick top performer
top_strat = max(perf.items(), key=lambda x: x[1]["pnl"])[0]

# Clone
child_strat = f"{top_strat}_mut_{random.randint(1000,9999)}"

# Load lineage
with open(LINEAGE_PATH) as f:
    lineage = json.load(f)

parent_depth = lineage[top_strat]["depth"]
lineage[child_strat] = {
    "parent": top_strat,
    "depth": parent_depth + 1,
    "sharpe": 0,
    "rating": "🧪 New Mutant"
}

with open(LINEAGE_PATH, "w") as f:
    json.dump(lineage, f, indent=2)

print(f"🧬 Cloned & mutated {top_strat} → {child_strat}")
