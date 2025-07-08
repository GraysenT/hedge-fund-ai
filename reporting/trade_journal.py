import json
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
ORDERS_PATH = "memory/order_logs"
JOURNAL_PATH = "reporting/trade_journal.json"

def explain_trade(trade):
    prompt = f"""
Explain why this trade was likely made.

Strategy: {trade['strategy']}
Symbol: {trade['symbol']}
Action: {trade['action']}
Confidence: {trade['confidence']}
Capital: {trade['capital']}

Give 2–3 bullet points.
"""
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return res["choices"][0]["message"]["content"]

def run():
    latest = sorted(os.listdir(ORDERS_PATH))[-1]
    trades = json.load(open(f"{ORDERS_PATH}/{latest}"))

    journal = {}
    for t in trades:
        t["explanation"] = explain_trade(t)
        journal[t["timestamp"]] = t

    with open(JOURNAL_PATH, "w") as f:
        json.dump(journal, f, indent=2)

    print(f"📓 Logged {len(journal)} trades with explanations.")

if __name__ == "__main__":
    run()
    