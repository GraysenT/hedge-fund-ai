import pandas as pd
import random
import json
import os

SIGNAL_LOG = "logs/signal_events.json"
RESULTS_FILE = "memory/adversarial_results.json"

def run_adversarial_tests():
    if not os.path.exists(SIGNAL_LOG):
        return

    with open(SIGNAL_LOG) as f:
        df = pd.DataFrame(json.load(f))

    tests = []
    for strategy in df["strategy"].unique():
        base = df[df["strategy"] == strategy]
        if len(base) < 5:
            continue

        # Simulate poisoning
        poisoned = base.copy()
        poisoned["confidence"] = poisoned["confidence"].apply(lambda x: x - random.uniform(0.2, 0.5))

        drop_rate = (poisoned["confidence"] < 0.4).mean()
        tests.append({
            "strategy": strategy,
            "confidence_drop_rate": round(drop_rate, 3),
            "fragile": drop_rate > 0.4
        })

    with open(RESULTS_FILE, "w") as f:
        json.dump(tests, f, indent=2)

    print(f"🧪 Adversarial test completed for {len(tests)} strategies.")
    return tests

if __name__ == "__main__":
    run_adversarial_tests()