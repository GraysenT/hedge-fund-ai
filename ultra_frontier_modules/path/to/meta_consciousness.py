import json
import copy


class MetaConsciousness:

    def __init__(self, system):
        self.system = system

    def analyze(self):
        return json.dumps(self.system, default=lambda o: o.__dict__)

    def reinvent(self, new_system):
        self.system = copy.deepcopy(new_system)
        return self.system