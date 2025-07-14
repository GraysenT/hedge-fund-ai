import json
from training.rl_agent import RLAgent

# Load dream-signal log
with open("logs/brain.jsonl") as f:
    logs = []
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            logs.append(json.loads(line))
        except json.JSONDecodeError as e:
            print(f"⚠️ Skipped invalid line: {e}")

agent = RLAgent()

for record in logs:
    try:
        state = str(record['dream']['context']['price'])  # Use price as simple state
        action = record['signal']
        reward = float(record['dream']['future_price']) - float(record['dream']['context']['price'])
        next_state = state  # Static for now; can be changed to future context
        agent.update(state, action, reward, next_state)
    except Exception as e:
        print(f"⚠️ Error processing record at tick {record.get('tick')}: {e}")

print("✅ RL training complete.")
print("🧠 Sample Q-values:", list(agent.q_table.items())[:5])