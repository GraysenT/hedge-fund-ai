from strategies.stat_arb_engine import generate_stat_arb_signals
from execution.stat_arb_executor import execute_stat_arb_signals

def run():
    print("🚀 Running scheduled stat arb signal cycle...")
    signals = generate_stat_arb_signals()
    if not signals.empty:
        execute_stat_arb_signals(signals)
    else:
        print("🟡 No stat arb signals triggered.")

if __name__ == "__main__":
    run()
    