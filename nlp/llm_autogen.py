import openai
import os
from nlp.strategy_compiler import save_strategy, run_in_sandbox

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_strategy():
    prompt = """
Write a simple Python strategy that uses price history to decide whether to buy or hold TSLA.
Print "BUY" if the price increased 3 days in a row. Else, print "HOLD".
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    code = generate_strategy()
    name = "auto_" + str(abs(hash(code)))[:6]
    save_strategy(code, name)
    run_in_sandbox(name)
