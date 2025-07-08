import subprocess

def run():
    print("\n🚀 Running Phase 4: Portfolio Learning & Risk Control")

    steps = [
        ("🛑 Step 1: Signal Veto", "execution.signal_veto"),
        ("🧠 Step 2: Volatility-Aware Reinforcement", "reinforcement.reward_agent"),
        ("🔁 Step 3: Portfolio Rotation", "portfolio_ai.rotation_engine"),
        ("💼 Step 4: Capital-at-Risk", "risk_control.capital_at_risk")
    ]

    for label, module in steps:
        print(f"\n{label}")
        try:
            subprocess.run(["python3", "-m", module], check=True)
        except subprocess.CalledProcessError:
            print(f"❌ Error in {module}")

    print("\n✅ Phase 4 complete.")

if __name__ == "__main__":
    run()
