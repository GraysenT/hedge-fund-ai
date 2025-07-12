class MemoryRecycler:
    def __init__(self):
        self.archive = []

    def recycle(self, memory_block):
        if len(memory_block) > 1000:
            retained = memory_block[-500:]  # Keep only the last 500 entries
            self.archive.append(memory_block[:-500])
            print(f"[MEMORY RECYCLE] Archived {len(memory_block[:-500])} entries.")
            return retained
        return memory_block

    def get_archive(self):
        return self.archive