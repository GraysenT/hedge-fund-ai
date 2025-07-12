class AgentMemoryWeaver:
    def __init__(self):
        self.memory = {}

    def weave_memory(self, agent_name, memory_content):
        """Merges memory and insight across recursive minds."""
        self.memory[agent_name] = memory_content
        print(f"Weaved memory for {agent_name}: {memory_content}")

    def get_memory(self):
        return self.memory