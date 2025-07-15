import os

MAX_LOG_SIZE_MB = 10

def enforce_log_limits():
    for file in os.listdir("logs/trades"):
        path = f"logs/trades/{file}"
        if os.path.getsize(path) > MAX_LOG_SIZE_MB * 1024 * 1024:
            os.remove(path)