import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def parse_abstract(text):
    prompt = f"""
You're a quant strategy generator. Given this research abstract, extract:
- Trading logic
- Risk model
- Asset class
- Timeframe

Then propose a Python signal framework (pseudocode or code block).

Abstract:
{text}
"""
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    print("📘 Strategy Idea:\n", res["choices"][0]["message"]["content"])

if __name__ == "__main__":
    text = input("📥 Paste abstract:\n")
    parse_abstract(text)
    