from datetime import datetime
from signal_generator import get_signals
from strategy_router.strategy_router import route_signal
from execution.signal_executor import execute_signal
from execution.signal_logger import log_signals
from performance.performance_tracker import log_daily_performance
from evolution.snapshot_saver import save_evolution_snapshot
from reinforcement.self_label_agent import reinforce
from ai.autonomous_upgrader import run_autonomous_upgrade_cycle

def main():
    print("🚀 Starting Trading System Main Loop")

    # 🧠 Step 1: Get today's signals
    signals_df = get_signals()

    # 🧠 Step 2: Route signals based on strategy weights, confidence, triggers
    routed_df = route_signal(signals_df)

    # 📝 Step 3: Log signals for audit and learning
    log_signals(routed_df)

    # ⚙️ Step 4: Execute valid signals
    for _, row in routed_df.iterrows():
        execute_signal(row)

    # 📊 Step 5: Log daily performance
    today = datetime.utcnow().strftime("%Y-%m-%d")
    log_daily_performance(
        date=today,
        pnl_dict={},  # fill in with actual PnL results
        capital_dict={},  # fill in with capital used
        sharpe_dict={}  # fill in with strategy Sharpe
    )

    # 🧠 Step 6: Save system snapshot
    save_evolution_snapshot()

    # ♻️ Step 7: Run autonomous improvement logic
    run_autonomous_upgrade_cycle()

    print("✅ Main cycle complete.")

if __name__ == "__main__":
    main()