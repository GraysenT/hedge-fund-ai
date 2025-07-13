from .interface_engine import submit_operator_command
from .request_registry import load_requests

def simulate_human_command():
    id = submit_operator_command("graysen", "Please reduce exposure to long duration bonds", category="override")
    return load_requests()

if __name__ == "__main__":
    from pprint import pprint
    pprint(simulate_human_command())