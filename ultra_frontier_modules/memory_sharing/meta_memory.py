import json


class MetaMemory:

    def __init__(self):
        self.memory = {}

    def save(self, key, value):
        self.memory[key] = value

    def load(self, key):
        return self.memory.get(key)

    def share(self, node):
        node.save(json.dumps(self.memory))

    def update(self, data):
        self.memory.update(json.loads(data))