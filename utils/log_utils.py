import os
import shutil
import time

def rotate_log(filepath, max_size_kb=200, backup_count=5):
    if not os.path.exists(filepath):
        return

    if os.path.getsize(filepath) > max_size_kb * 1024:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        rotated_file = f"{filepath}.{timestamp}.bak"
        shutil.copy(filepath, rotated_file)
        with open(filepath, "w") as f:
            f.write("[]")
        print(f"[LOG ROTATION] Rotated {filepath} to {rotated_file}")

def log_event(event):
    print(f'Event: {event}')