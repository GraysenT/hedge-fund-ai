import pandas as pd
from portfolio_ai.multi_agent_router import split_weights_across_accounts

def build_account_signal_dict(global_signal_df: pd.DataFrame, strategy_weights: dict, account_ids: list):
    """
    Build a dict of signals routed to each account based on strategy weights.

    Returns:
        account_signal_dict: { account_id: pd.DataFrame of filtered signals }
    """
    # Step 1: Split weights across accounts
    account_weights = split_weights_across_accounts(strategy_weights, account_ids)

    # Step 2: Filter signals per account based on that account's strategy weights
    account_signal_dict = {}

    for account in account_ids:
        acct_weights = account_weights[account]
        filtered = global_signal_df[global_signal_df["strategy"].isin(acct_weights.keys())].copy()

        # Optionally: apply account-specific weight to confidence
        for strat, weight in acct_weights.items():
            filtered.loc[filtered["strategy"] == strat, "confidence"] *= weight

        account_signal_dict[account] = filtered

    return account_signal_dict