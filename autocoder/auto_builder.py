import os
import json
import time
from autocoder.codegen_engine import generate_module
from autocoder.auto_ideator import append_to_queue
from reinforcement.recursive_generator import append_mutations_to_queue
from utils.paths import MODULE_QUEUE_FILE
from utils.logger import log_event
import ast

BUILD_DIR = "."

def is_valid_python(code):
    try:
        ast.parse(code)
        return True
    except SyntaxError as e:
        print(f"[VALIDATION] Syntax error: {e}")
        return False

def load_queue():
    if not os.path.exists(MODULE_QUEUE_FILE):
        return {}
    with open(MODULE_QUEUE_FILE, "r") as f:
        return json.load(f)

def build_all():
    # Inject new ideas and mutations
    append_to_queue()
    append_mutations_to_queue()

    queue = load_queue()
    built_count = 0

    for path, desc in queue.items():
        full_path = os.path.join(BUILD_DIR, path)
        if os.path.exists(full_path):
            continue  # Already built

        log_event(f"🛠️ Building: {path} — {desc}")
        print(f"🛠️ Generating: {path}")

        code = generate_module(desc, filename=path)

        if not is_valid_python(code):
            log_event(f"❌ Syntax failed: {path}")
            continue

        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(code)

        log_event(f"✅ Module passed syntax and saved: {path}")
        built_count += 1

        if built_count >= 5:
            break  # Limit batch size per run

    if built_count == 0:
        log_event("ℹ️ No new modules built this cycle.")

if __name__ == "__main__":
    while True:
        build_all()
        time.sleep(120)  # Every 2 minutes