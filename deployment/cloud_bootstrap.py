import os
import subprocess
from utils.config_loader import load_config

def launch():
    config = load_config()
    if config.get("cloud_mode", False):
        print("🚀 Cloud bootstrap running...")
        subprocess.Popen(["python", "deployment/main.py"])

if __name__ == "__main__":
    launch()