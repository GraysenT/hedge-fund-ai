import os
import json
from meta.meta_strategy_engine import run_meta_strategy_scoring
from reinforcement.self_label_agent import update_self_labels
from reinforcement.simulation_memory import update_simulation_memory
from reinforcement.research_feedback import integrate_research_feedback
from strategy_router.deployment_router import apply_deployability_filters
from strategy_router.strategy_voter import run_strategy_vote
from portfolio_ai.full_allocator import update_strategy_weights
from dashboards.phase5_dashboard import log_phase5_summary
from risk_control.alpha_defense import check_alpha_integrity
from risk_control.adversarial_adaptation import adapt_to_adversity
from portfolio_ai.fund_allocator import allocate_across_funds
from meta.meta_agent import run_meta_agent_cycle
from analytics.performance_attribution import generate_alpha_attribution
from risk_control.global_risk_matrix import generate_risk_matrix
from meta.deployability_scorer import score_strategy_deployability
from risk_control.confidence_risk_score import score_confidence_vs_risk
from portfolio_ai.capital_optimizer import optimize_capital_allocation
from reporting.investor_report_generator import generate_investor_report

REQUIRED_MEMORY_FILES = [
    "memory/deployability_scores.json",
    "memory/confidence_vs_risk.json",
    "memory/optimized_allocations.json",
    "memory/alpha_attribution.json",
    "memory/global_risk_matrix.json",
    "logs/trade_history.json"
]

def validate_and_repair_memory():
    print("\n🔎 Checking system memory files...")
    for path in REQUIRED_MEMORY_FILES:
        if not os.path.exists(path) or os.stat(path).st_size == 0:
            print(f"⚠️ Missing or empty: {path}")
            if "deployability" in path:
                score_strategy_deployability()
            elif "confidence" in path:
                score_confidence_vs_risk()
            elif "optimized_allocations" in path:
                optimize_capital_allocation()
            elif "alpha_attribution" in path:
                generate_alpha_attribution()
            elif "global_risk_matrix" in path:
                generate_risk_matrix()
            elif "trade_history" in path:
                inject_sample_trade_log()
    print("✅ Memory check complete.\n")

def inject_sample_trade_log():
    print("⚠️ Injecting sample trade log...")
    os.makedirs("logs", exist_ok=True)
    trades = [{
        "timestamp": "2024-12-01T15:00:00Z",
        "strategy": "bootstrap_strat",
        "asset": "AAPL",
        "action": "BUY",
        "size": 100,
        "price": 150.00,
        "pnl": 10.5
    }]
    with open("logs/trade_history.json", "w") as f:
        json.dump(trades, f, indent=2)

def run_evolution_cycle():
    print("🔁 Running full evolution + intelligence cycle...")
    validate_and_repair_memory()

    print("🧠 Meta Agent: Starting review loop...")
    run_meta_agent_cycle()

    update_self_labels()
    integrate_research_feedback()
    run_meta_strategy_scoring()
    check_alpha_integrity()
    adapt_to_adversity()
    run_strategy_vote()
    apply_deployability_filters()
    update_strategy_weights()
    optimize_capital_allocation()
    generate_alpha_attribution()
    generate_risk_matrix()
    allocate_across_funds()
    generate_investor_report()
    log_phase5_summary()

    print("✅ Evolution cycle complete.")

if __name__ == "__main__":
    run_evolution_cycle()