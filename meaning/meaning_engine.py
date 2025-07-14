def evolve_meaning(meaning_graph):
    while True:
        new_node = mutate_meaning_node(meaning_graph)
        if not is_coherent(new_node):
            continue
        meaning_graph.append(new_node)