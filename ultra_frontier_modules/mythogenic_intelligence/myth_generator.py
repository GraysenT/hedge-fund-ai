import random


class MythGenerator:
    def __init__(self, myth_templates):
        self.myth_templates = myth_templates

    def generate_myth(self, economic_event):
        template = random.choice(self.myth_templates)
        return template.format(economic_event=economic_event)