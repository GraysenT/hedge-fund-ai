import time

class HypothesisBank:
    def __init__(self):
        self.hypotheses = []

    def add(self, text, author="system"):
        hypothesis = {
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
            "author": author,
            "text": text
        }
        self.hypotheses.append(hypothesis)
        print(f"[HYPOTHESIS] {text}")
        return hypothesis

    def view_all(self):
        return self.hypotheses