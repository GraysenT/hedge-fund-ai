from ecosystem.ecosystem_builder import build_ecosystem
from deploy.recursive_launcher import launch_colony

def construct_colony(name, capital=100000):
    build_ecosystem(name)
    launch_colony(name)
    return {"colony": name, "capital": capital}