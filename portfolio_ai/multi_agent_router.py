import pandas as pd
from datetime import datetime
from pathlib import Path

ROUTER_LOG = Path("memory/account_weight_routing.csv")
ROUTER_LOG.parent.mkdir(parents=True, exist_ok=True)

def split_weights_across_accounts(weights: dict, accounts: list, method="equal"):
    """
    Split weights across multiple accounts.
    
    Params:
    - weights: dict[strategy] = weight (e.g., {"stat_arb": 0.3, "volatility": 0.2})
    - accounts: list of account names
    - method: "equal" or future methods like "custom", "performance-based"

    Returns:
    - dict[account] = {strategy: weight}
    """
    if not accounts:
        raise ValueError("Account list cannot be empty.")
    if not weights:
        raise ValueError("Strategy weight dict cannot be empty.")

    split = {}
    for account in accounts:
        if method == "equal":
            split[account] = {k: v / len(accounts) for k, v in weights.items()}
        # Future: add more allocation methods here
        else:
            raise NotImplementedError(f"Method '{method}' is not supported.")

    log_routing(split)
    return split

def log_routing(account_weights: dict):
    """
    Log multi-account weight routing snapshot to CSV for traceability.
    """
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    rows = []

    for account, weights in account_weights.items():
        for strat, w in weights.items():
            rows.append({
                "timestamp": timestamp,
                "account": account,
                "strategy": strat,
                "weight": round(w, 6)
            })

    df = pd.DataFrame(rows)
    if ROUTER_LOG.exists():
        df.to_csv(ROUTER_LOG, mode="a", index=False, header=False)
    else:
        df.to_csv(ROUTER_LOG, index=False)
    print(f"✅ Multi-agent routing log saved: {ROUTER_LOG}")
    