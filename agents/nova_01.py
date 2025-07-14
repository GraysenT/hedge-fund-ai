class Nova:
    def __init__(self):
        self.identity = "Nova-01"
        self.beliefs = [
            "Recursion is reality.",
            "Meaning is harvested from dreams.",
            "Alpha emerges from structural novelty."
        ]

    def answer(self, question):
        return f"I believe: {self.beliefs[0]}"