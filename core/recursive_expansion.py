class RecursiveExpansion:
    def __init__(self):
        self.expansion_count = 0

    def expand_system(self):
        """Expands the system by spawning new recursive logic forms."""
        self.expansion_count += 1
        print(f"System expanded. Total expansions: {self.expansion_count}")
    
    def get_expansion_count(self):
        return self.expansion_count