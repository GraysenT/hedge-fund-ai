def retrieve_memory(query):
    memory_index = {'alpha': 'Alpha strategy memory', 'beta': 'Beta memory chunk'}
    return memory_index.get(query, 'Memory not found')