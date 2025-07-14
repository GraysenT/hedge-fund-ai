import json
import os

def deploy_to_fork(strategy, fork_id):
    os.makedirs(f"forks/{fork_id}", exist_ok=True)
    with open(f"forks/{fork_id}/{strategy['name']}.json", "w") as f:
        json.dump(strategy, f)