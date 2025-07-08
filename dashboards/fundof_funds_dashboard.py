import json
import os

def show_fundof_funds_dashboard():
    path = "memory/fund_weights.json"
    if not os.path.exists(path):
        print("❌ No FoF weights found.")
        return

    with open(path) as f:
        data = json.load(f)

    print("\n📊 Fund-of-Funds Allocator Weights:")
    for fund, weight in data.items():
        print(f" - {fund}: {weight * 100:.2f}%")

if __name__ == "__main__":
    show_fundof_funds_dashboard()