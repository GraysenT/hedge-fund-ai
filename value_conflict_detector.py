```python
class DecisionNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []
        self.flag = False

    def add_child(self, node):
        self.children.append(node)

    def evaluate_conflicts(self, parent_value=None):
        if parent_value and self.value != parent_value:
            self.flag = True
        for child in self.children:
            child.evaluate_conflicts(self.value)

def build_decision_graph():
    # Example graph construction
    root = DecisionNode("Root", "speed")
    child1 = DecisionNode("Child1", "speed")
    child2 = DecisionNode("Child2", "safety")
    child1_1 = DecisionNode("Child1_1", "speed")
    child1_2 = DecisionNode("Child1_2", "safety")
    child2_1 = DecisionNode("Child2_1", "safety")

    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(child1_1)
    child1.add_child(child1_2)
    child2.add_child(child2_1)

    return root

def print_decision_graph(node, depth=0):
    flag_status = "FLAGGED" if node.flag else "OK"
    print("  " * depth + f"{node.name} ({node.value}) - {flag_status}")
    for child in node.children:
        print_decision_graph(child, depth + 1)

def main():
    root = build_decision_graph()
    root.evaluate_conflicts()
    print_decision_graph(root)

if __name__ == "__main__":
    main()
```