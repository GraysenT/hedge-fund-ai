import os
import json
from datetime import datetime

class EvolutionSaver:
    def __init__(self, folder="snapshots"):
        self.folder = folder
        os.makedirs(folder, exist_ok=True)

    def save(self, weights: dict, muted: list, alerts: list, alpha_report: dict):
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"evolution_{today}.json"
        path = os.path.join(self.folder, filename)

        data = {
            "timestamp": datetime.now().isoformat(),
            "weights": weights,
            "muted": muted,
            "alerts": alerts,
            "alpha_health": alpha_report
        }

        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        return path
