import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def load_context():
    with open("agents/agent_tournament_results.json") as f:
        agents = json.load(f)

    with open("strategy_memory/strategy_lineage.json") as f:
        lineage = json.load(f)

    with open("plugins/plugin_log.json") as f:
        plugins = json.load(f)

    return agents, lineage, plugins

def ask_committee():
    agents, lineage, plugins = load_context()
    prompt = f"""
You're an AI investment committee. You must decide which strategies to:
1. Promote
2. Retire
3. Mutate

Use the agent tournament data:\n{agents}
Use strategy lineage:\n{list(lineage.keys())[-5:]}
Use plugin logs:\n{list(plugins.items())[-3:]}

Give only three lists: [Promote], [Retire], [Mutate].
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    print("🧠 Committee Response:")
    print(response["choices"][0]["message"]["content"])

if __name__ == "__main__":
    ask_committee()
    