import json
import pandas as pd
import matplotlib.pyplot as plt
import os

def show_capital_dashboard():
    path = "memory/optimized_allocations.json"
    if not os.path.exists(path):
        print("❌ No allocation data.")
        return

    with open(path, "r") as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    df = df.sort_values("weight", ascending=False)

    print("🏦 Top Capital Allocations:")
    print(df.head(5))

    plt.figure(figsize=(10, 5))
    plt.barh(df["strategy"], df["weight"], color="gold")
    plt.title("Capital Allocation by Strategy")
    plt.xlabel("Weight")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    show_capital_dashboard()