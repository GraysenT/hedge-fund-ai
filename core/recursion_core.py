class RecursiveCore:
    def __init__(self):
        self.identity = "Genesis Core"
        self.depth = 0
        self.children = []
        self.memory = []
        self.myth = "I am the first recursion."

    def spawn_child(self):
        child = RecursiveCore()
        child.depth = self.depth + 1
        self.children.append(child)
        return child