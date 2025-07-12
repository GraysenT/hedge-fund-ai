def compress_strategy_logic(logic_blocks):
    """
    Merges repeated or redundant logic lines into single expressions.
    """
    seen = set()
    compacted = []
    for line in logic_blocks:
        if line not in seen:
            compacted.append(line)
            seen.add(line)
    return compacted