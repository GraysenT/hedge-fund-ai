import os

CHECKLIST = [
    "docker-compose.yml",
    "runloop.py",
    "evolve.py",
    "dashboards/control_center.py",
    "execution/execution_router.py",
    "meta/meta_strategy_engine.py",
    "reinforcement/self_label_agent.py"
]

def check_deployment():
    print("🧾 Deployment Readiness Checklist")
    for file in CHECKLIST:
        exists = os.path.exists(file)
        print(f"{file}: {'✅ OK' if exists else '❌ MISSING'}")

if __name__ == "__main__":
    check_deployment()