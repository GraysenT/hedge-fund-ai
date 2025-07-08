import random

def simulate_branch(parent, depth, max_depth=5):
    if depth > max_depth:
        return {}
    children = {}
    for _ in range(random.randint(1, 3)):
        child = f"{parent}_d{depth}_{random.randint(100,999)}"
        children[child] = simulate_branch(child, depth + 1)
    return children

def display_tree(tree, indent=0):
    for node, subtree in tree.items():
        print("  " * indent + f"🔁 {node}")
        display_tree(subtree, indent + 1)

if __name__ == "__main__":
    root = "gen_strat_seed"
    tree = simulate_branch(root, 1)
    print("🌳 Simulated Evolution Tree:\n")
    display_tree(tree)
    