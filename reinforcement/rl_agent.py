import random
import json
import os

Q_TABLE_PATH = "reinforcement/rl_q_table.json"

states = ["low_vol", "high_vol", "bullish", "bearish"]
actions = ["buy", "sell", "hold"]

# Simple reward logic
def simulate_reward(state, action):
    return random.uniform(-1, 1) if action != "hold" else 0.1

def update_q_table(q_table, alpha=0.1, gamma=0.9):
    for state in states:
        if state not in q_table:
            q_table[state] = {a: 0 for a in actions}
        for action in actions:
            reward = simulate_reward(state, action)
            future = max(q_table[state].values())
            q_table[state][action] += alpha * (reward + gamma * future - q_table[state][action])
    return q_table

def save_q_table(q_table):
    with open(Q_TABLE_PATH, "w") as f:
        json.dump(q_table, f, indent=2)
    print("🎯 RL Agent Q-table updated.")

if __name__ == "__main__":
    if os.path.exists(Q_TABLE_PATH):
        with open(Q_TABLE_PATH, "r") as f:
            q_table = json.load(f)
    else:
        q_table = {}

    q_table = update_q_table(q_table)
    save_q_table(q_table)
