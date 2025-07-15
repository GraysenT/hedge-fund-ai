ontology_map = {}

def register_ontology(colony, rules):
    ontology_map[colony] = rules

def translate_belief(belief, source_colony, target_colony):
    source = ontology_map.get(source_colony, {})
    target = ontology_map.get(target_colony, {})
    return target.get(belief, belief)