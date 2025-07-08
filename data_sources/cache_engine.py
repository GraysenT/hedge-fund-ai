import os
import pandas as pd
import pickle
from hashlib import sha256

def cache_key(symbol, start, end):
    return sha256(f"{symbol}_{start}_{end}".encode()).hexdigest()

def load_from_cache(symbol, start, end):
    key = cache_key(symbol, start, end)
    filepath = f".cache/{key}.pkl"
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            return pickle.load(f)
    return None

def save_to_cache(symbol, start, end, df):
    os.makedirs(".cache", exist_ok=True)
    key = cache_key(symbol, start, end)
    filepath = f".cache/{key}.pkl"
    with open(filepath, 'wb') as f:
        pickle.dump(df, f)