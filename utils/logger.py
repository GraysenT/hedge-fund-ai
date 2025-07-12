from datetime import datetime
from utils.paths import SELF_BUILD_LOG

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(SELF_BUILD_LOG, "a") as f:
        f.write(f"[{timestamp}] {message}\n")