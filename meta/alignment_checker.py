import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def check_alignment(strategy_path):
    with open(strategy_path, "r") as f:
        code = f.read()

    prompt = f"""
You're a policy enforcement bot.

Review this strategy code. Check if it:
- Uses only equity tickers
- Avoids leverage
- Follows momentum or macro style
- Respects volatility < 2%

Return PASS or FAIL and explain.

Code:
{code}
"""

    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    print("🧭 Alignment Check:\n", res["choices"][0]["message"]["content"])

if __name__ == "__main__":
    check_alignment("plugins/sample_strategy.py")
    