import json, os
from autogen.gpt_writer import generate_phase_modules  # Reuse your GPT caller
from datetime import datetime

QUEUE_PATH = "openai_api/api_queue.json"
LOG_PATH = "openai_api/task_log.json"
OUT_DIR = "ultra_frontier_modules"

def load_queue():
    with open(QUEUE_PATH, "r") as f:
        return json.load(f)

def save_queue(tasks):
    with open(QUEUE_PATH, "w") as f:
        json.dump(tasks, f, indent=2)

def log_result(task, modules):
    os.makedirs("openai_api", exist_ok=True)
    log = []
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r") as f:
            log = json.load(f)
    log.append({
        "id": task["id"],
        "title": task["title"],
        "timestamp": datetime.now().isoformat(),
        "files": [m["path"] for m in modules],
    })
    with open(LOG_PATH, "w") as f:
        json.dump(log, f, indent=2)

def run_next_task():
    tasks = load_queue()
    for task in tasks:
        if task["status"] == "pending":
            print(f"🚀 Running task: {task['title']}")
            phase_data = {
                "title": task["title"],
                "description": task["description"]
            }
            modules = generate_phase_modules(phase_data)
            for m in modules:
                path = os.path.join(OUT_DIR, m["path"])
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w") as f:
                    f.write(m["code"])
            task["status"] = "done"
            save_queue(tasks)
            log_result(task, modules)
            print(f"✅ Task complete: {task['id']}")
            return
    print("🟡 No pending tasks.")

if __name__ == "__main__":
    run_next_task()