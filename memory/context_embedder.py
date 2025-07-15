def embed_context(context):
    return hash(str(context)) % 1_000_000
