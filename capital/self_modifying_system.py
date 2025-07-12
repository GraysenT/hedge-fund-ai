class SelfModifyingSystem:
    def __init__(self):
        self.modifications = []

    def apply_modification(self, modification_type, modification_factor):
        """Apply recursive system modifications autonomously."""
        modification = {"modification_type": modification_type, "modification_factor": modification_factor}
        self.modifications.append(modification)
        print(f"Applied modification: {modification_type} with factor: {modification_factor}")
    
    def get_modifications(self):
        return self.modifications