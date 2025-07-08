import json
import os

CLIENTS = {
    "clientA": {"base_fee": 100, "pnl_cut": 0.15},
    "clientB": {"base_fee": 75, "pnl_cut": 0.10}
}

def compute_fees():
    alloc_path = sorted(os.listdir("memory/client_allocations"))[-1]
    allocs = json.load(open(f"memory/client_allocations/{alloc_path}"))
    
    perf_path = sorted(os.listdir("memory/performance"))[-1]
    perf = json.load(open(f"memory/performance/{perf_path}"))

    invoices = {}
    for client, strategies in allocs.items():
        fee = CLIENTS[client]["base_fee"]
        pnl_total = 0
        for strat in strategies:
            if strat in perf:
                pnl_total += perf[strat]["pnl"]
        bonus = max(0, pnl_total * CLIENTS[client]["pnl_cut"])
        invoices[client] = round(fee + bonus, 2)

    print("🧾 Client Invoices:")
    for client, amount in invoices.items():
        print(f"{client}: ${amount}")

if __name__ == "__main__":
    compute_fees()
    