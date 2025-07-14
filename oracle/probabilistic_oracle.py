from oracle.probabilistic_oracle import predict
import random

def predict(event):
    return {
        "event": event,
        "confidence": round(random.uniform(0.3, 0.95), 2),
        "basis": "Recursive trend lineage"
    }

def ask_oracle(event):
    result = predict(event)
    print(result)