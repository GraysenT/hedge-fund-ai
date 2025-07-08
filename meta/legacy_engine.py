import json
import os
from datetime import datetime

LINEAGE = "strategy_memory/strategy_lineage.json"
GRAVEYARD = "strategy_memory/graveyard.json"
LEGACY_LOG = "meta/legacy_retired.json"

def retire_lineages():
    lineage = json.load(open(LINEAGE))
    graveyard = json.load(open(GRAVEYARD)) if os.path.exists(GRAVEYARD) else {}

    children_by_parent = {}
    for strat, meta in lineage.items():
        parent = meta.get("parent", "ROOT")
        children_by_parent.setdefault(parent, []).append(strat)

    retired_families = []
    for parent, children in children_by_parent.items():
        if all(c in graveyard for c in children):
            retired_families.append(parent)

    archive = {p: {"retired_on": datetime.now().isoformat(), "reason": "all children dead"} for p in retired_families}
    json.dump(archive, open(LEGACY_LOG, "w"), indent=2)
    print("⚰️ Retired Lineages:")
    for p in retired_families:
        print(f" - {p}")

if __name__ == "__main__":
    retire_lineages()
    