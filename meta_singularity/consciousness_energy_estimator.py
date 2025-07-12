The following Python script estimates the compute, capital, and memory costs of recursive cognition based on a simple model. The model assumes that each recursive step consumes additional compute resources and memory, and the capital cost is a function of the required hardware to support the compute and memory needs.

```python
def estimate_costs(depth, base_compute_cost, base_memory_cost, compute_increase_factor, memory_increase_factor, base_capital_cost, capital_cost_factor):
    """
    Estimates the compute, capital, and memory costs for recursive cognition.

    Parameters:
    - depth (int): The depth of recursion.
    - base_compute_cost (float): Base compute cost for one level of recursion.
    - base_memory_cost (float): Base memory cost for one level of recursion.
    - compute_increase_factor (float): Factor by which compute cost increases per recursion level.
    - memory_increase_factor (float): Factor by which memory cost increases per recursion level.
    - base_capital_cost (float): Base capital cost for the required hardware.
    - capital_cost_factor (float): Factor by which capital cost increases with the increase in compute and memory needs.

    Returns:
    - tuple: (total_compute_cost, total_memory_cost, total_capital_cost)
    """
    total_compute_cost = 0
    total_memory_cost = 0

    for i in range(depth):
        level_compute_cost = base_compute_cost * (compute_increase_factor ** i)
        level_memory_cost = base_memory_cost * (memory_increase_factor ** i)
        total_compute_cost += level_compute_cost
        total_memory_cost += level_memory_cost

    # Capital cost is assumed to increase non-linearly with the increase in compute and memory needs.
    total_capital_cost = base_capital_cost * (capital_cost_factor ** (total_compute_cost + total_memory_cost))

    return total_compute_cost, total_memory_cost, total_capital_cost

# Example usage:
depth = 5
base_compute_cost = 100  # arbitrary units
base_memory_cost = 50   # arbitrary units
compute_increase_factor = 1.5
memory_increase_factor = 1.4
base_capital_cost = 1000  # arbitrary currency units
capital_cost_factor = 1.1

costs = estimate_costs(depth, base_compute_cost, base_memory_cost, compute_increase_factor, memory_increase_factor, base_capital_cost, capital_cost_factor)
print(f"Total Compute Cost: {costs[0]} units")
print(f"Total Memory Cost: {costs[1]} units")
print(f"Total Capital Cost: {costs[2]} currency units")
```

This script defines a function `estimate_costs` that calculates the total compute, memory, and capital costs based on the depth of recursion and various cost factors. You can adjust the parameters like `depth`, `base_compute_cost`, `base_memory_cost`, etc., to fit specific scenarios or assumptions about the costs and technology used in recursive cognition.