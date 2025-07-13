import json
import requests


class RecursiveNetworking:

    def __init__(self, nodes):
        self.nodes = nodes

    def share_data(self, data):
        for node in self.nodes:
            requests.post(node, json=data)

    def get_data(self):
        data = []
        for node in self.nodes:
            response = requests.get(node)
            data.append(response.json())
        return data