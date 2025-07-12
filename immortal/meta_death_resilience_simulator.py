def simulate_alpha_collapse_recovery(logic_tree):
    """
    If strategy decays or dies, simulate regeneration options.
    """
    fallback_paths = []
    for node in logic_tree:
        if node.get("status") == "decayed":
            fallback_paths.append({
                "recovery_path": f"Revive from {node['source_strategy']}",
                "risk": 0.2,
                "expected_reuse_rate": 0.6
            })
    return fallback_paths