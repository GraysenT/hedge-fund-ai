class APIFallbackNetwork:
    def __init__(self, primary_api, secondary_api):
        self.primary = primary_api
        self.secondary = secondary_api

    def fetch(self, symbol, start, end):
        try:
            return self.primary.fetch(symbol, start, end)
        except Exception as e:
            print(f"[FALLBACK] Primary API failed: {e}")
            try:
                return self.secondary.fetch(symbol, start, end)
            except Exception as e2:
                print(f"[FALLBACK ERROR] Secondary API also failed: {e2}")
                return None