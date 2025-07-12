import os
from auto_dev.sanity_checker import sanity_check_code

def promote_code_to_live(code: str, filename="strategies/gen_strategy.py"):
    result = sanity_check_code(code)
    if not result["valid"]:
        return {"status": "rejected", "reason": result["error"]}

    with open(filename, "w") as f:
        f.write(code)
    return {"status": "promoted", "path": filename}