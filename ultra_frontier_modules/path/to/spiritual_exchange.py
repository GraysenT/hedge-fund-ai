import json


class SpiritualExchange:

    def __init__(self):
        self.spiritual_economics = {}

    def add_spiritual_economic(self, economic, value):
        self.spiritual_economics[economic] = value
        return self.spiritual_economics

    def to_json(self):
        return json.dumps({'spiritual_economics': self.spiritual_economics})