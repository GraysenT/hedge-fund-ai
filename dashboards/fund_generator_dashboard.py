import os
import json

def show_fund_generator_dashboard():
    print("\n🧠 Virtual Fund Generator Dashboard:")
    path = "memory/funds_generated"
    if not os.path.exists(path):
        print("❌ No generated funds yet.")
        return

    files = os.listdir(path)
    for f in files:
        with open(os.path.join(path, f)) as data:
            strategies = json.load(data)
        print(f" - {f}: {len(strategies)} strategies")

if __name__ == "__main__":
    show_fund_generator_dashboard()