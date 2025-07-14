from multiprocessing import Process
import os
import time

markets = ["ETHUSD", "BTCUSD", "AAPL", "SPX", "SOLUSD"]
agents = []

for market in markets:
    cmd = f"python3 deploy/city_server.py {market}"
    agents.append(Process(target=os.system, args=(cmd,)))

print("🌍 Launching agents...")
for agent in agents:
    agent.start()
    time.sleep(2)