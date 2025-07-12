def evaluate_and_govern(logic_cells):
    """
    Scores and governs logic cells by survivability, performance, and coherence.
    """
    survivors = []
    for cell in logic_cells:
        if cell.get("coherence", 0) > 0.7 and cell.get("score", 0) > 0:
            survivors.append(cell)
    return survivors