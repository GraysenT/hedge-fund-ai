import os
import json

def show_fund_dashboard():
    base_path = "memory/funds"
    if not os.path.exists(base_path):
        print("❌ No fund data found.")
        return

    print("\n📊 Multi-Fund Allocation Overview")
    for fund in os.listdir(base_path):
        path = os.path.join(base_path, fund, "allocations.json")
        if os.path.exists(path):
            with open(path, "r") as f:
                data = json.load(f)
            print(f" - {fund}: {len(data)} strategies")

if __name__ == "__main__":
    show_fund_dashboard()