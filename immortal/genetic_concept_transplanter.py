def transplant_logic_traits(parent_logic, traits_to_reuse):
    """
    Transfers selected logic features into a new signal structure.
    """
    new_logic = parent_logic[:]
    for trait in traits_to_reuse:
        if trait not in new_logic:
            new_logic.append(trait)
    return new_logic