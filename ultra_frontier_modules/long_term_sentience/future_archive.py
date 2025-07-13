import json
import os
from datetime import datetime

ARCHIVE_PATH = "memory/forecast_archive.json"

def save_future_path(path, score, tag=""):
    archive = []
    if os.path.exists(ARCHIVE_PATH):
        with open(ARCHIVE_PATH, "r") as f:
            archive = json.load(f)

    entry = {
        "timestamp": datetime.now().isoformat(),
        "score": score,
        "tag": tag,
        "timeline": path
    }
    archive.append(entry)

    with open(ARCHIVE_PATH, "w") as f:
        json.dump(archive, f, indent=2)