class BeliefMesh:
    def __init__(self):
        self.mesh = {}  # key = context, value = ContextBelief object

    def register_belief(self, belief_obj):
        self.mesh[belief_obj.context] = belief_obj

    def update_belief(self, context, new_strength):
        if context in self.mesh:
            self.mesh[context].update_belief(new_strength)

    def compute_mesh_entropy(self):
        """
        Returns how conflicted or uniform the belief space is.
        Closer to 0 = high alignment, Closer to 1 = full chaos.
        """
        values = [b.strength for b in self.mesh.values()]
        if not values:
            return 0.0
        avg = sum(values) / len(values)
        variance = sum((v - avg) ** 2 for v in values) / len(values)
        return round(variance ** 0.5, 3)

    def export_mesh(self):
        return {k: v.serialize() for k, v in self.mesh.items()}