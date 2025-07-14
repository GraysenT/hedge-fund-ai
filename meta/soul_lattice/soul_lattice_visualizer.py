def visualize_lattice(agent_souls):
    print('Visualizing Soul Lattice:')
    for soul in agent_souls:
        print(soul['agent'], '->', soul['soul_vector'])