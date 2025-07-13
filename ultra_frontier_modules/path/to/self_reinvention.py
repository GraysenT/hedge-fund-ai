import json


class SelfReinvention:

    def __init__(self, system):
        self.system = system

    def reinvent_logic(self, new_logic):
        self.system.logic = new_logic
        return self.system

    def reinvent_architecture(self, new_architecture):
        self.system.architecture = new_architecture
        return self.system

    def reinvent_purpose(self, new_purpose):
        self.system.purpose = new_purpose
        return self.system