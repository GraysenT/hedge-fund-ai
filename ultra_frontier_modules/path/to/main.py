from multiverse import Multiverse


if __name__ == '__main__':
    multiverse = Multiverse()
    multiverse.add_history('universe1', [1, 2, 3])
    multiverse.add_history('universe2', [4, 5, 6])
    multiverse.add_future('universe1', [7, 8, 9])
    multiverse.add_future('universe2', [10, 11, 12])

    divergence = multiverse.get_divergence('universe1', 'universe2')
    print(f'Divergence: {divergence}')

    convergence = multiverse.get_convergence('universe1', 'universe2')
    print(f'Convergence: {convergence}')