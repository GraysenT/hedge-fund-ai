"""
Main autonomous execution loop for the hedge fund AI system.
- Routes strategies
- Applies patches
- Executes orders
- Logs trades and signals
"""

import time
import json
import os
from execution.strategy_router import route_all_strategies
from execution.execution_router import route_order
from utils.paths import TRADE_LOG_FILE, SIGNAL_LOG
from utils.log_utils import rotate_log
from intelligence.multi_agent_orchestrator import *
import time
import random
import os
for agent in agents:
    agent.self_upgrade()

os.environ['ALPACA_API_KEY'] = "your_key_here"
os.environ['ALPACA_SECRET_KEY'] = "your_secret_here"
os.environ['OPENAI_API_KEY'] = "your_openai_key_here"

def get_live_market_state():
    return {
        'momentum': random.uniform(-1, 1),
        'volatility': random.uniform(10, 40),
        'gdp_growth': random.uniform(1, 4),
        'social_sentiment': random.uniform(0, 1),
        'news_score': random.uniform(0, 1),
        'rsi': random.randint(10, 90),
        'correlation': random.uniform(-1, 1),
        'liquidity': random.randint(0, 100)
    }

if __name__ == "__main__":
    agents = [
        StrategyAgent("StratA"),
        RiskAgent("RiskControl"),
        MacroAgent("MacroAgent"),
        SentimentAgent("SentimentAgent"),
        NewsAgent("NewsAgent"),
        TechnicalAgent("TechnicalAgent"),
        CorrelationAgent("CorrelationAgent"),
        LiquidityAgent("LiquidityAgent"),
        GPTReflectiveAgent("MetaAgentGPT")
    ]
    orchestrator = MultiAgentOrchestrator(agents)

    print("\n=== GLOBAL REAL-TIME TRADING CONSCIOUSNESS ===")
    for _ in range(20):
        state = get_live_market_state()
        result = orchestrator.run(state)
        print(result)
        time.sleep(1)


rotate_log(TRADE_LOG_FILE)
rotate_log(SIGNAL_LOG)

def run_main_cycle():
    print("📈 Starting Hedge Fund AI Main Loop...")

    # Step 1: Route signals
    signals = route_all_strategies()

    # Step 2: Execute each signal
    executed_trades = {}
    for strategy_name, signal in signals.items():
        try:
            result = route_order(strategy_name, signal)
            executed_trades[strategy_name] = result
        except Exception as e:
            print(f"[EXECUTION ERROR] {strategy_name}: {e}")
            executed_trades[strategy_name] = {"status": "error", "error": str(e)}

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # Step 3: Log trade execution
    trade_entry = {
        "timestamp": timestamp,
        "signals": signals,
        "executions": executed_trades
    }

    if not os.path.exists(TRADE_LOG_FILE):
        with open(TRADE_LOG_FILE, "w") as f:
            json.dump([], f)

    try:
        with open(TRADE_LOG_FILE, "r") as f:
            trade_log = json.load(f)
            if not isinstance(trade_log, list):
                print("⚠️ trade_log.json was not a list. Resetting.")
                trade_log = []
    except json.JSONDecodeError:
        print("⚠️ trade_log.json was corrupted. Resetting.")
        trade_log = []

    trade_log.append(trade_entry)

    with open(TRADE_LOG_FILE, "w") as f:
        json.dump(trade_log, f, indent=2)

    # Step 4: Log raw signals for history tracking
    signal_entry = {
        "timestamp": timestamp,
        "signals": signals
    }

    if not os.path.exists(SIGNAL_LOG):
        with open(SIGNAL_LOG, "w") as f:
            json.dump([], f)

    try:
        with open(SIGNAL_LOG, "r") as f:
            signal_log = json.load(f)
            if not isinstance(signal_log, list):
                print("⚠️ signal_log.json was not a list. Resetting.")
                signal_log = []
    except json.JSONDecodeError:
        print("⚠️ signal_log.json was corrupted. Resetting.")
        signal_log = []

    signal_log.append(signal_entry)

    with open(SIGNAL_LOG, "w") as f:
        json.dump(signal_log, f, indent=2)

    print("✅ Cycle complete.\n")

if __name__ == "__main__":
    while True:
        run_main_cycle()
        time.sleep(1)  # Run once per second