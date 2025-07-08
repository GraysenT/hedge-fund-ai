import os
import json
from datetime import datetime

print("🚀 Booting Hedge Fund AI system...")

os.makedirs("logs", exist_ok=True)
os.makedirs("memory", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# 1. Inject sample trade history
trade_log_path = "logs/trade_history.json"
if not os.path.exists(trade_log_path) or os.stat(trade_log_path).st_size == 0:
    trade_log = [{
        "timestamp": "2024-12-01T15:00:00Z",
        "strategy": "stat_arb",
        "asset": "AAPL",
        "action": "BUY",
        "size": 100,
        "price": 150.00,
        "pnl": 25.50
    }]
    with open(trade_log_path, "w") as f:
        json.dump(trade_log, f, indent=2)
    print("✅ Injected sample trade history.")

# 2. Inject sample research hypothesis
hypo_path = "memory/research_memory.json"
if not os.path.exists(hypo_path) or os.stat(hypo_path).st_size == 0:
    research = [{
        "id": "h1",
        "idea": "MACD and RSI divergence predicts mean reversion",
        "context": "Applied to SPY, QQQ, AAPL",
        "score": 0.85,
        "timestamp": datetime.utcnow().isoformat()
    }]
    with open(hypo_path, "w") as f:
        json.dump(research, f, indent=2)
    print("✅ Injected sample hypothesis.")

# 3. Run all generators in order
os.system("python3 meta/deployability_scorer.py")
os.system("python3 risk_control/confidence_risk_score.py")
os.system("python3 portfolio_ai/capital_optimizer.py")
os.system("python3 analytics/performance_attribution.py")
os.system("python3 risk_control/global_risk_matrix.py")
os.system("python3 reporting/investor_report_generator.py")

# 4. Unlock system (delete lock flag)
lock_flag = "memory/deployment_locked.flag"
if os.path.exists(lock_flag):
    os.remove(lock_flag)
    print("🔓 Deployment unlocked.")

print("✅ Boot complete. You can now run:")
print("   → python3 evolve.py")
print("   → python3 runloop.py")