import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def score_plugin(path):
    with open(path, "r") as f:
        code = f.read()

    prompt = f"""
Rate this trading strategy code from 1–10 in:

1. Logic quality
2. Risk control
3. Code readability
4. Potential for overfitting

Provide brief comments for each.

Code:
{code}
"""

    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    print("🧪 Code Score:\n", res["choices"][0]["message"]["content"])

if __name__ == "__main__":
    score_plugin("plugins/sample_strategy.py")
    