from scale.market_awareness import get_market_status
import os

def show_global_scaling_dashboard():
    print("\n🌍 Global Market Coverage Dashboard")
    status = get_market_status()
    for region, open_status in status.items():
        print(f"{region:<7}: {open_status}")

    rep_path = "strategies/replicated/"
    if os.path.exists(rep_path):
        files = os.listdir(rep_path)
        print(f"\n🧬 Replicated Strategies ({len(files)} total):")
        for f in files[:10]:
            print(" -", f)

if __name__ == "__main__":
    show_global_scaling_dashboard()