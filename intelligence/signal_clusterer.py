from collections import defaultdict

class SignalClusterer:
    def __init__(self):
        self.clusters = defaultdict(list)

    def cluster(self, signal):
        key = f"{signal['symbol']}_{signal['action']}"
        self.clusters[key].append(signal)
        print(f"[CLUSTER] Added to {key}: Confidence={signal['confidence']}")
        return key

    def get_cluster(self, key):
        return self.clusters.get(key, [])