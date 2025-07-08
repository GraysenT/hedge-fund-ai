import os
import time
from datetime import datetime
from models.retrainer import retrain_lstm

def get_symbols_to_retrain():
    return ["AAPL", "TSLA", "MSFT"]  # Extendable

def run():
    symbols = get_symbols_to_retrain()
    for sym in symbols:
        retrain_lstm(sym)

if __name__ == "__main__":
    while True:
        now = datetime.now()
        if now.hour == 21 and now.minute == 0:  # 9:00 PM
            run()
            time.sleep(60)
        else:
            time.sleep(30)
