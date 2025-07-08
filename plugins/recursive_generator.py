import openai
import os
from nlp.strategy_compiler import save_strategy, run_in_sandbox

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_plugin():
    prompt = """
Write a Python plugin that creates a strategy which buys a stock after 3 green candles.
The plugin should create a `run()` function that dynamically writes another plugin
called `auto_child_plugin.py` containing the strategy logic, and saves it to /plugins/.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def install_and_run_plugin():
    code = generate_plugin()
    name = "recursive_plugin"
    save_strategy(code, name)
    run_in_sandbox(name)

if __name__ == "__main__":
    install_and_run_plugin()
