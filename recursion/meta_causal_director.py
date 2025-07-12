def orchestrate_logic_flow(modules, system_goals):
    """
    Directs which logical modules run, in what order, based on strategic purpose alignment.
    """
    directed_modules = []
    for mod in modules:
        if any(goal in mod.get("tags", []) for goal in system_goals):
            directed_modules.append(mod)
    return sorted(directed_modules, key=lambda x: x.get("priority", 1))