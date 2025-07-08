import os
import json
from collections import defaultdict

LINEAGE_PATH = "strategy_memory/strategy_lineage.json"
CLAN_TAG_PATH = "strategy_memory/strategy_clans.json"


def tag_clans():
    if not os.path.exists(LINEAGE_PATH):
        raise FileNotFoundError("strategy_lineage.json not found")

    with open(LINEAGE_PATH, 'r') as f:
        lineage = json.load(f)

    # Build reverse map and track root ancestors
    parent_map = {child: meta["parent"] for child, meta in lineage.items() if "parent" in meta and meta["parent"] != child}
    if not parent_map:
        print("⚠️ No valid parent-child relationships found in lineage.")
        return

    def find_root(s):
        while s in parent_map:
            s = parent_map[s]
        return s

    clans = defaultdict(list)
    for child in lineage:
        root = find_root(child)
        clans[root].append(child)

    # Flatten and tag
    clan_tags = {}
    for root, members in clans.items():
        for strat in members:
            clan_tags[strat] = f"clan_{root}"

    with open(CLAN_TAG_PATH, 'w') as f:
        json.dump(clan_tags, f, indent=2)

    print(f"✅ Tagged {len(clan_tags)} strategies into {len(clans)} clans.")
    for root, members in clans.items():
        print(f"  🧬 {root}: {len(members)} members")


if __name__ == '__main__':
    tag_clans()