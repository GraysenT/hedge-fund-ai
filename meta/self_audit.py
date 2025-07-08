import os
import json

def run_self_audit():
    issues = []

    # Allocation sanity
    alloc_path = sorted(os.listdir("memory/scaled_allocations"))[-1]
    allocs = json.load(open(f"memory/scaled_allocations/{alloc_path}"))
    total = sum(allocs.values())
    if total < 0.9 or total > 1.1:
        issues.append(f"💥 Capital allocation anomaly: {total * 100:.2f}%")

    # Plugin result check
    plugins = json.load(open("plugins/plugin_log.json"))
    for name, log in plugins.items():
        if log.get("error"):
            issues.append(f"🔧 Plugin {name} failed: {log['error']}")

    print("✅ Self-audit complete.")
    for issue in issues:
        print(f"⚠️ {issue}")

if __name__ == "__main__":
    run_self_audit()
    