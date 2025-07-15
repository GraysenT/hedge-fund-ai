from memory.ontological_memory import similarity_search
from lang.llm_interface import generate_response

def ask_agent(query):
    hits = similarity_search(query)
    context = "\n".join(hit["source"] for hit in hits[:5])
    return generate_response(query, context)