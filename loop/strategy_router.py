from strategies.fork_engine import deploy_to_fork

def route_strategy(strategy, fork_id):
    deploy_to_fork(strategy, fork_id)