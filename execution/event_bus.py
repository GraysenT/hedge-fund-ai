from queue import Queue
bus = Queue()

def publish(msg):
    bus.put(msg)

def subscribe():
    return bus.get()