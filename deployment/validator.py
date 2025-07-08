import os
from pathlib import Path

REQUIRED_FOLDERS = ["snapshots", "execution_logs", "memory", "performance_logs"]
REQUIRED_FILES = [
    "memory/meta_blended_weights.csv",
    "audit/fund_balance.csv",
    "memory/alpha_defense_status.csv"
]

def validate_system():
    print("🔒 Validating deployment structure...")
    success = True

    for folder in REQUIRED_FOLDERS:
        if not Path(folder).exists():
            print(f"❌ Missing folder: {folder}")
            success = False

    for file in REQUIRED_FILES:
        if not Path(file).exists():
            print(f"❌ Missing file: {file}")
            success = False

    if success:
        print("✅ All critical components found. System is deployable.")
    else:
        print("⚠️ Deployment check failed. See above.")