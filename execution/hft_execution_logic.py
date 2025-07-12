import time

class HFTExecutionLogic:
    def __init__(self, max_latency=0.01):
        self.max_latency = max_latency  # Maximum allowed latency in seconds
        self.execution_times = []

    def execute_trade(self, trade_type, price, size):
        """Execute a trade with minimal latency and track execution time."""
        start_time = time.time()
        # Simulate order execution
        time.sleep(self.max_latency)  # Simulating network delay or execution delay
        end_time = time.time()
        
        execution_time = end_time - start_time
        self.execution_times.append(execution_time)
        
        # Placeholder for actual trade logic (send order to exchange, etc.)
        print(f"Executed {trade_type} trade: Price = {price}, Size = {size}, Latency = {execution_time}s")

        # Check if latency is within acceptable limits
        if execution_time > self.max_latency:
            print(f"Warning: Execution latency exceeded the limit: {execution_time}s")

    def get_average_execution_time(self):
        return sum(self.execution_times) / len(self.execution_times) if self.execution_times else 0
