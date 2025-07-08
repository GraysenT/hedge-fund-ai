import requests
import os
import json

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, json=payload)

def handle_command(cmd):
    if cmd == "/capital":
        path = "memory/scaled_allocations/" + sorted(os.listdir("memory/scaled_allocations"))[-1]
        with open(path) as f:
            caps = json.load(f)
        lines = [f"{k}: ${round(v*1_000_000, 2)}" for k, v in caps.items()]
        send_message("💸 Capital Allocations:\n" + "\n".join(lines))

    elif cmd == "/trades":
        path = "memory/order_logs/" + sorted(os.listdir("memory/order_logs"))[-1]
        with open(path) as f:
            trades = json.load(f)
        msgs = [f"{o['strategy']} {o['action'].upper()} {o['qty']} {o['symbol']} @ ${o['price']}" for o in trades]
        send_message("📈 Recent Trades:\n" + "\n".join(msgs))

    elif cmd == "/top_agents":
        with open("agents/agent_tournament_results.json") as f:
            results = json.load(f)
        top = sorted(results.items(), key=lambda x: x[1]["pnl"], reverse=True)[:3]
        msgs = [f"{a}: ${round(s['pnl'],2)}" for a, s in top]
        send_message("🏆 Top Agents:\n" + "\n".join(msgs))

    else:
        send_message("🤖 Unknown command.")

if __name__ == "__main__":
    # Simulate incoming command
    handle_command("/capital")  # Replace this with live polling in production
