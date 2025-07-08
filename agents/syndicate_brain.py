import os
import json
from datetime import datetime

MEMORY_PATH = "agents/syndicates/memory/"
PROPOSALS_PATH = "agents/syndicates/proposals/"

SYNDICATES = {
    "macro_alpha": ["agent_macro", "agent_defensive"],
    "short_vol": ["agent_shield", "agent_fast"],
    "momentum_lstm": ["agent_mom", "agent_lstm"]
}

def log_trade(syndicate, strategy, pnl):
    os.makedirs(MEMORY_PATH, exist_ok=True)
    mem_file = os.path.join(MEMORY_PATH, f"{syndicate}.json")
    memory = json.load(open(mem_file)) if os.path.exists(mem_file) else []
    memory.append({
        "strategy": strategy,
        "pnl": pnl,
        "timestamp": datetime.now().isoformat()
    })
    json.dump(memory, open(mem_file, "w"), indent=2)
    print(f"🧠 Logged trade to {syndicate} memory.")

def vote_on_proposal(syndicate, strategy, summary):
    os.makedirs(PROPOSALS_PATH, exist_ok=True)
    file = os.path.join(PROPOSALS_PATH, f"{syndicate}_{datetime.now().strftime('%Y%m%d')}.json")
    proposal = {
        "strategy": strategy,
        "summary": summary,
        "votes": {agent: "yes" for agent in SYNDICATES[syndicate]}
    }
    json.dump(proposal, open(file, "w"), indent=2)
    print(f"🗳 {syndicate} submitted proposal: {strategy}")

if __name__ == "__main__":
    log_trade("macro_alpha", "gen_strat_r2", 75.2)
    vote_on_proposal("macro_alpha", "macro_alpha_rsi_x", "Trades Fed-forward regime breaks.")
    