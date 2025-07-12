"""
Main evolution loop that scores, reinforces, mutates, and updates strategy performance.
"""

import time
from reinforcement.self_label_agent import self_label_and_reinforce
from strategy_router.strategy_voter import run_strategy_voting
from strategy_router.deployment_router import run_deployment_filter
from alerts.strategy_triggers import mute_strategy, reward_strategy
from meta.meta_feedback import update_strategy_scores
from reinforcement.recursive_generator import append_mutations_to_queue
from utils.logger import log_event

def run_evolution_cycle():
    print("🧠 Starting evolution cycle...")

    # Step 1: Update performance scores (Sharpe, win rate, etc.)
    update_strategy_scores()

    # Step 2: Reinforce based on past behavior
    self_label_and_reinforce()

    # Step 3: Vote and deploy strategies
    approved = run_strategy_voting()
    deployed = run_deployment_filter(approved)

    # Step 4: Reward/deprioritize based on outcome
    for strat in deployed:
        reward_strategy(strat)
    for strat in approved:
        if strat not in deployed:
            mute_strategy(strat)

    # Step 5: Generate mutated strategy variants
    append_mutations_to_queue()

    log_event(f"✅ Evolution cycle complete: {len(deployed)} strategies deployed.")
    print(f"✅ Evolution cycle complete. {len(deployed)} strategies remain active.\n")

if __name__ == "__main__":
    while True:
        run_evolution_cycle()
        time.sleep(1800)  # 30 minutes per evolution cycle