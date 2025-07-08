import json
import os

def show_alpha_agent_dashboard():
    path = "memory/reinforcement_rewards.json"
    if not os.path.exists(path):
        print("❌ No reward log.")
        return

    with open(path) as f:
        data = json.load(f)

    print("\n🧠 Reinforcement Alpha Agent Dashboard")
    for d in data[:5]:
        print(f"{d['id']} → reward: {d['reward']}")

if __name__ == "__main__":
    show_alpha_agent_dashboard()