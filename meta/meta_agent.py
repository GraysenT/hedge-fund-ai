import time
import random
from reporting.investor_report_generator import generate_investor_report
from analytics.performance_attribution import generate_alpha_attribution
from reinforcement.simulation_memory import update_simulation_memory

def run_meta_agent_cycle():
    print("\n🧠 Meta Agent: Starting review loop...")
    
    generate_alpha_attribution()
    update_simulation_memory()
    report = generate_investor_report()

    pnl = report['summary']["Total PnL"]
    trades = report['summary']["Total Trades"]
    print(f"🧠 Meta Agent: PnL={pnl}, Trades={trades}")

    if pnl < 0 and trades > 10:
        print("⚠️ Meta Agent: Detected poor performance. Suggest reducing risk or quarantining.")
    elif pnl > 1000:
        print("🚀 Meta Agent: High alpha detected — recommend replication and scaling.")
    else:
        print("📈 Meta Agent: Stable. Monitoring...")

if __name__ == "__main__":
    while True:
        run_meta_agent_cycle()
        time.sleep(600)  # every 10 minutes