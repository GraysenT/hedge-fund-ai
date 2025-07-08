def split_allocations(weights, accounts):
    """
    Distribute weights across N accounts based on desired structure.
    """
    splits = {}
    for account in accounts:
        splits[account] = {k: v / len(accounts) for k, v in weights.items()}
    return splits
    