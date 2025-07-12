```python
class LogicGate:
    def __init__(self, label):
        self.label = label
        self.output = None
        self.inputs = []

    def perform_gate_logic(self):
        raise NotImplementedError("Must implement in subclass")

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

    def add_input(self, input_gate):
        self.inputs.append(input_gate)

    def __str__(self):
        return f"{self.label}: {self.get_output()}"

class AndGate(LogicGate):
    def perform_gate_logic(self):
        result = 1
        for input_gate in self.inputs:
            result = result and input_gate.get_output()
        return result

class OrGate(LogicGate):
    def perform_gate_logic(self):
        result = 0
        for input_gate in self.inputs:
            result = result or input_gate.get_output()
        return result

class NotGate(LogicGate):
    def perform_gate_logic(self):
        if len(self.inputs) != 1:
            raise ValueError("NotGate must have exactly one input")
        return not self.inputs[0].get_output()

class Connector:
    def __init__(self, from_gate, to_gate):
        self.from_gate = from_gate
        self.to_gate = to_gate
        to_gate.add_input(from_gate)

    def __str__(self):
        return f"{self.from_gate.label} -> {self.to_gate.label}"

class InputGate(LogicGate):
    def __init__(self, label, state):
        super().__init__(label)
        self.state = state

    def perform_gate_logic(self):
        return self.state

    def set_state(self, state):
        self.state = state

def trace_signal_path(gate, path=None):
    if path is None:
        path = []

    if isinstance(gate, InputGate):
        path.append(f"Input {gate.label} ({gate.get_output()})")
    else:
        path.append(f"{gate.label} ({gate.get_output()})")

    for input_gate in gate.inputs:
        trace_signal_path(input_gate, path)

    return path

# Example usage
if __name__ == "__main__":
    # Create input gates
    g1 = InputGate("G1", 1)
    g2 = InputGate("G2", 0)

    # Create logic gates
    and_gate = AndGate("AND1")
    or_gate = OrGate("OR1")
    not_gate = NotGate("NOT1")

    # Connect gates
    Connector(g1, and_gate)
    Connector(g2, and_gate)
    Connector(and_gate, or_gate)
    Connector(g2, or_gate)
    Connector(or_gate, not_gate)

    # Trace the signal path
    output_path = trace_signal_path(not_gate)
    print(" -> ".join(reversed(output_path)))
```