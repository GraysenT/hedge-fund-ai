import pandas as pd
import os
from collections import defaultdict
from datetime import datetime

def build_logic_tree(hypotheses_df):
    tree = defaultdict(lambda: defaultdict(list))

    for _, row in hypotheses_df.iterrows():
        asset = row["Asset"]
        strategy = row["Strategy"]
        signal = row["Signal"]
        confidence = row["Confidence Range"]
        tree[asset][strategy].append((signal, confidence))

    return tree

def print_tree(tree):
    print("\n🌿 Strategy Logic Tree:")
    for asset, strat_dict in tree.items():
        print(f"\n📦 {asset}")
        for strategy, branches in strat_dict.items():
            print(f"  ├─ 🧠 {strategy}")
            for signal, conf in branches:
                print(f"  │   └─ {signal} @ {conf}")

def run():
    print("\n🌿 Logic Tree Constructor Running...")

    memory_path = "logs/research_memory.csv"
    tree_output = "logs/logic_tree_snapshot.txt"

    if not os.path.exists(memory_path):
        print("❌ No research memory found.")
        return

    df = pd.read_csv(memory_path)
    if df.empty:
        print("ℹ️ No ideas in research memory.")
        return

    tree = build_logic_tree(df)
    print_tree(tree)

    # Save snapshot
    with open(tree_output, "w") as f:
        f.write("Logic Tree Snapshot - " + datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC\n\n"))
        for asset, strat_dict in tree.items():
            f.write(f"\n{asset}\n")
            for strategy, branches in strat_dict.items():
                f.write(f"  {strategy}\n")
                for signal, conf in branches:
                    f.write(f"    - {signal} @ {conf}\n")

    print(f"\n✅ Logic tree saved to {tree_output}")

if __name__ == "__main__":
    run()
    