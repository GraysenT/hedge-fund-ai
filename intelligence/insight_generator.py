from gpt_reasoning_engine import GPTReasoningEngine
from memory.agent_memory_store import AgentMemoryStore

def generate_insight():
    engine = GPTReasoningEngine()
    memory = AgentMemoryStore().load()
    prompt = "What trends, ideas, or weaknesses can you spot in the hedge fund strategy network?"
    return engine.ask(prompt, memory)

if __name__ == "__main__":
    insight = generate_insight()
    print("🧠 Insight Report:\n", insight)