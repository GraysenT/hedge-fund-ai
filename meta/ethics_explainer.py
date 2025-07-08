import openai
import json
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def explain_ethics(action, strategy_meta):
    constitution = json.load(open("meta/constitution.json"))
    prompt = f"""
You are the ethics officer of an AI fund.

Evaluate the following action:
{action}

Strategy metadata:
{strategy_meta}

Fund Constitution:
{constitution}

Return: PASS/FAIL, and explanation in 3 bullet points.
"""
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    print("🧭 Ethics Summary:\n")
    print(res["choices"][0]["message"]["content"])

if __name__ == "__main__":
    example_meta = {
        "model": "LSTM",
        "confidence": 0.76,
        "sector": "tech",
        "style": "momentum"
    }
    explain_ethics("Deploy strategy gen_strat_r8 using 1.5x leverage", example_meta)
    