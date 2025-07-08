import pandas as pd

def load_sp500():
    url = "https://datahub.io/core/s-and-p-500-companies/r/constituents.csv"
    df = pd.read_csv(url)
    return df["Symbol"].tolist()

def load_nasdaq100():
    url = "https://raw.githubusercontent.com/datasets/nasdaq-listings/master/data/nasdaq-listed-symbols.csv"
    df = pd.read_csv(url)
    return df["Symbol"].tolist()[:100]

def get_universe():
    return sorted(set(load_sp500() + load_nasdaq100()))

if __name__ == "__main__":
    symbols = get_universe()
    print(f"✅ Loaded {len(symbols)} symbols:")
    print(symbols[:10])
