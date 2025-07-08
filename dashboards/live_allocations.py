import pandas as pd
import json

def show_live_allocations():
    df = pd.read_json("memory/optimized_allocations.json")
    print(df.sort_values("weight", ascending=False))

if __name__ == "__main__":
    show_live_allocations()