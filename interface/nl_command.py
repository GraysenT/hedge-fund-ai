import re
import json
import os

def interpret(command: str):
    cmd = command.lower()

    if "top agents" in cmd:
        print("📊 Fetching top agents...")
        with open("agents/agent_tournament_results.json") as f:
            data = json.load(f)
        ranked = sorted(data.items(), key=lambda x: x[1]["pnl"], reverse=True)
        for agent, stats in ranked[:5]:
            print(f"🏆 {agent}: ${round(stats['pnl'],2)} over {stats['days']} days")

    elif "latest trades" in cmd:
        print("📈 Showing recent trades...")
        path = "memory/order_logs/" + sorted(os.listdir("memory/order_logs"))[-1]
        with open(path) as f:
            orders = json.load(f)
        for o in orders:
            print(f"{o['strategy']} → {o['action'].upper()} {o['qty']} {o['symbol']} @ ${o['price']}")

    elif "show" in cmd and "capital" in cmd:
        print("💸 Allocated capital:")
        cap_path = "memory/scaled_allocations/" + sorted(os.listdir("memory/scaled_allocations"))[-1]
        with open(cap_path) as f:
            caps = json.load(f)
        for strat, amt in caps.items():
            print(f"{strat}: ${round(amt*1_000_000, 2)}")

    else:
        print("🤖 I didn’t understand that. Try: 'show top agents', 'latest trades', or 'capital allocations'.")

if __name__ == "__main__":
    while True:
        query = input("🔍 Ask a question: ")
        interpret(query)
