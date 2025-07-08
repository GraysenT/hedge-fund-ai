import importlib.util
import traceback
import os
import json
from datetime import datetime

LOG_PATH = "plugins/plugin_log.json"

def run_in_sandbox(plugin_name):
    path = f"plugins/{plugin_name}.py"
    spec = importlib.util.spec_from_file_location(plugin_name, path)
    mod = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(mod)
        output = mod.run() if hasattr(mod, "run") else "⚠️ No run()"
        log_result(plugin_name, output, None)
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
        "private": True  # 🔐 private flag enabled
    }

    with open(LOG_PATH, "w") as f:
        json.dump(logs, f, indent=2)
    print(f"🔒 Plugin {name} run logged (private: ✅)")

if __name__ == "__main__":
    run_in_sandbox("sample_strategy")
