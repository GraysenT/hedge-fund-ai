import time
import subprocess
from datetime import datetime

def run_once():
    print(f"📆 Recursion Runner Starting: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    subprocess.call(["python3", "-m", "reinforcement.recursive_generator"])
    print("✅ Recursive evolution complete.\n")

if __name__ == "__main__":
    # Example: Run daily at 2:00 AM local time
    TARGET_HOUR = 2
    TARGET_MIN = 0

    while True:
        now = datetime.now()
        if now.hour == TARGET_HOUR and now.minute == TARGET_MIN:
            run_once()
            time.sleep(60)  # avoid multiple runs in the same minute
        else:
            time.sleep(30)
