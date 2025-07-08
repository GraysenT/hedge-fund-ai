import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def explain_backtest(strategy_name):
    path = sorted(os.listdir("memory/performance"))[-1]
    perf = json.load(open(f"memory/performance/{path}"))
    result = perf.get(strategy_name)

    if not result:
        print("❌ No data.")
        return

    prompt = f"""
Explain why this strategy may have performed the way it did:

Name: {strategy_name}
PNL: {result['pnl']}
Return %: {round(result['return_pct']*100, 2)}

Be specific about risk, drawdown, and possible market behavior.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    print("🧠 Strategy Analysis:\n", response["choices"][0]["message"]["content"])

if __name__ == "__main__":
    explain_backtest("gen_strat_r2")
