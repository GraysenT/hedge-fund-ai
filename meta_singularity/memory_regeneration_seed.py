```python
import pickle
import os

class SeedManager:
    def __init__(self, backup_path):
        self.backup_path = backup_path
        self.seeds = {}
        self.load_seeds()

    def load_seeds(self):
        if os.path.exists(self.backup_path):
            with open(self.backup_path, 'rb') as file:
                self.seeds = pickle.load(file)
        else:
            self.seeds = {}

    def save_seeds(self):
        with open(self.backup_path, 'wb') as file:
            pickle.dump(self.seeds, file)

    def add_seed(self, identity, seed_data):
        self.seeds[identity] = seed_data
        self.save_seeds()

    def get_seed(self, identity):
        return self.seeds.get(identity, None)

    def remove_seed(self, identity):
        if identity in self.seeds:
            del self.seeds[identity]
            self.save_seeds()

# Example usage
backup_file = 'seed_backup.pkl'
seed_manager = SeedManager(backup_file)

# Adding a seed
seed_manager.add_seed('seed1', {'data': 'example data'})

# Retrieving a seed
print(seed_manager.get_seed('seed1'))

# Removing a seed
seed_manager.remove_seed('seed1')

# Check if the seed is removed
print(seed_manager.get_seed('seed1'))
```