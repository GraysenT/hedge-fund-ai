import threading, time
from runloop import run_main_cycle
from evolve import run_evolution_cycle

def launch_colony(name):
    t1 = threading.Thread(target=run_main_cycle, name=f"{name}_loop")
    t2 = threading.Thread(target=run_evolution_cycle, name=f"{name}_evolver")
    t1.start()
    t2.start()
    print(f"🚀 Launched colony: {name}")