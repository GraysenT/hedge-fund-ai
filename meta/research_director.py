import openai
import json
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def fetch_context():
    perf = sorted(os.listdir("memory/performance"))[-1]
    pnl = json.load(open(f"memory/performance/{perf}"))

    lineage = json.load(open("strategy_memory/strategy_lineage.json"))
    return pnl, lineage

def generate_directive():
    pnl, lineage = fetch_context()
    prompt = f"""
You're the AI Research Director for a hedge fund.

Review the following performance and strategy pool. Recommend:
- New strategy directions
- Which agents to focus on
- What to retire or improve
- Missing regimes or styles

Performance: {pnl}
Lineage: {list(lineage.keys())[-10:]}

Return a 3-point research plan.
"""
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return res["choices"][0]["message"]["content"]

if __name__ == "__main__":
    plan = generate_directive()
    print("📋 Research Director Plan:\n", plan)
    