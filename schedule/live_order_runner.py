from dotenv import load_dotenv
load_dotenv()
import os
import time
import subprocess
from datetime import datetime

TARGET_HOUR = 8
TARGET_MIN = 30

def run_order_flow():
    print("⏰ Triggering live order execution...")
    subprocess.call(["python3", "-m", "execution.order_router"])

while True:
    now = datetime.now()
    if now.weekday() < 5 and now.hour == TARGET_HOUR and now.minute == TARGET_MIN:
        run_order_flow()
        time.sleep(60)
    else:
        time.sleep(30)
