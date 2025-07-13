from collections import defaultdict

class ConvergenceGrid:
    def __init__(self):
        self.grid = defaultdict(list)

    def register_signal(self, signal):
        self.grid[signal.theme].append({
            "domain": signal.domain,
            "source": signal.source,
            "confidence": signal.confidence,
            "time": signal.timestamp
        })

    def detect_convergence(self, threshold=3, min_confidence=0.6):
        converging = []
        for theme, entries in self.grid.items():
            high_conf = [e for e in entries if e["confidence"] >= min_confidence]
            if len(high_conf) >= threshold:
                converging.append({
                    "theme": theme,
                    "sources": [e["source"] for e in high_conf],
                    "avg_confidence": round(sum(e["confidence"] for e in high_conf) / len(high_conf), 3),
                    "domains": list(set(e["domain"] for e in high_conf))
                })
        return converging