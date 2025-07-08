import json
import os
import pandas as pd

def show_adversarial_dashboard():
    path = "memory/adversarial_results.json"
    if not os.path.exists(path):
        print("❌ No adversarial results.")
        return

    with open(path) as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    print("\n🛡️ Signal Fragility Report")
    print(df.sort_values("confidence_drop_rate", ascending=False).head(5))

if __name__ == "__main__":
    show_adversarial_dashboard()