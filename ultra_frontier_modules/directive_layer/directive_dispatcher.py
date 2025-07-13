import os
import json

DIRECTIVE_LOG = "memory/sovereign_directives.json"

def load_directives():
    if not os.path.exists(DIRECTIVE_LOG):
        return []
    with open(DIRECTIVE_LOG, "r") as f:
        return json.load(f)

def save_directive(directive_obj):
    directives = load_directives()
    directives.append(directive_obj.serialize())
    with open(DIRECTIVE_LOG, "w") as f:
        json.dump(directives, f, indent=2)