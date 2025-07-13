from typing import Callable, List

class EventBus:
    def __init__(self):
        self.subscribers: List[Callable] = []

    def publish(self, event: dict):
        for sub in self.subscribers:
            sub(event)

    def subscribe(self, callback: Callable):
        self.subscribers.append(callback)