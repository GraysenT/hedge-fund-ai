import os
from datetime import datetime
import importlib.util
import json
import traceback

PLUGINS_DIR = "plugins"
LOG_PATH = "plugins/plugin_log.json"

def parse_instruction(instruction):
    if "RSI" in instruction and "above" in instruction:
        return f"""
def run():
    import pandas as pd
    df = pd.read_csv('data/price_history/TSLA.csv')
    df['rsi'] = df['close'].rolling(14).apply(lambda x: 100 - (100 / (1 + (x[-1]-x.mean())/x.std())))
    if df['rsi'].iloc[-1] > 70:
        print("BUY TSLA (RSI breakout)")
    else:
        print("HOLD")
"""

    return "# Could not interpret instruction"

def save_strategy(code, name):
    path = f"{PLUGINS_DIR}/{name}.py"
    with open(path, "w") as f:
        f.write(code)
    return path

def run_in_sandbox(plugin_name):
    path = f"{PLUGINS_DIR}/{plugin_name}.py"
    spec = importlib.util.spec_from_file_location(plugin_name, path)
    mod = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(mod)
        result = mod.run() if hasattr(mod, "run") else "⚠️ No run()"
        log_result(plugin_name, result, None)
    except Exception as e:
        error = traceback.format_exc()
        log_result(plugin_name, None, error)

def log_result(name, result, error):
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r") as f:
            logs = json.load(f)
    else:
        logs = {}

    logs[name] = {
        "last_run": datetime.now().isoformat(),
        "result": str(result),
        "error": str(error) if error else None,
        "private": True
    }

    with open(LOG_PATH, "w") as f:
        json.dump(logs, f, indent=2)
    print(f"🔁 Plugin {name} logged")

if __name__ == "__main__":
    instr = input("💬 Describe your strategy:\n")
    name = "compiled_" + str(abs(hash(instr)))[:6]
    code = parse_instruction(instr)
    save_strategy(code, name)
    run_in_sandbox(name)