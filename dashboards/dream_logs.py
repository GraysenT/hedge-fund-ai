from recursion.dream_logger import log_dream

# Example visualization
def display_dreams(agent_id):
    with open(f"logs/dreams/{agent_id}_dream.json") as f:
        data = f.read()
    print(f"Dream log for {agent_id}:\n{data}")