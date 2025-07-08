import os
import json
import random
import uuid

SOURCE_DIR = "strategies/"
REPLICATED_DIR = "strategies/replicated/"
os.makedirs(REPLICATED_DIR, exist_ok=True)

TARGET_MARKETS = ["EU", "ASIA", "LATAM", "FX", "CRYPTO", "FUTURES"]

def replicate_top_strategies():
    approved = "memory/deployment_approved.json"
    if not os.path.exists(approved):
        print("❌ No approved strategies.")
        return

    with open(approved, "r") as f:
        base_strats = json.load(f)

    for strat in base_strats[:3]:  # replicate top 3
        for market in TARGET_MARKETS:
            suffix = f"_{market.lower()}_{uuid.uuid4().hex[:4]}"
            new_file = f"replicated_{suffix}.py"
            src_lines = [
                f"# Replicated for {market} market\n",
                f"# Original Idea: {strat['idea'][:60]}...\n"
            ]
            src_lines += [
                f"# Adapted for {market} latency/volatility profile\n\n",
                "def strategy(data):\n",
                "    # Market adaptation logic placeholder\n",
                "    return 'BUY' if data['volatility'] < 0.02 else 'HOLD'\n"
            ]

            with open(os.path.join(REPLICATED_DIR, new_file), "w") as f:
                f.writelines(src_lines)

            print(f"🌐 Replicated strategy for {market}: {new_file}")

if __name__ == "__main__":
    replicate_top_strategies()