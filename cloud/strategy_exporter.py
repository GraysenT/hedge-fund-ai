import os
import json
from cloud.aws_uploader import upload_to_s3

LINEAGE_PATH = "strategy_memory/strategy_lineage.json"
PERF_PATH = "memory/performance"

latest_perf = sorted(os.listdir(PERF_PATH))[-1]
with open(os.path.join(PERF_PATH, latest_perf)) as f:
    perf = json.load(f)

# Pick top N
top = sorted(perf.items(), key=lambda x: x[1]["pnl"], reverse=True)[:5]
top_ids = [s[0] for s in top]

# Export mini snapshot
with open(LINEAGE_PATH) as f:
    lineage = json.load(f)

export = {k: lineage[k] for k in top_ids if k in lineage}
snapshot_path = "strategy_memory/top_strategies.json"
with open(snapshot_path, "w") as f:
    json.dump(export, f, indent=2)

upload_to_s3(snapshot_path, "shared_strategies/top_strategies.json")
