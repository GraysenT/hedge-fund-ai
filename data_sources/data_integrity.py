class DataIntegrityScanner:
    def __init__(self):
        self.flags = []

    def validate(self, df, source_name):
        if df.empty:
            self.flags.append((source_name, "Empty dataset"))
        if df.isnull().sum().sum() > 0:
            self.flags.append((source_name, "Missing values detected"))
        if not df.index.is_monotonic_increasing:
            self.flags.append((source_name, "Time index not sorted"))

        if self.flags:
            print(f"[DATA INTEGRITY] Issues found in {source_name}: {self.flags}")
        return not self.flags