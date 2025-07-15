treaties = {}

def propose_treaty(e1, e2, terms):
    key = f"{e1}_{e2}"
    treaties[key] = terms
    return f"Treaty proposed between {e1} and {e2}"

def get_treaty(e1, e2):
    return treaties.get(f"{e1}_{e2}") or treaties.get(f"{e2}_{e1}")