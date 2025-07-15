from multiprocessing import Process

def run_strategy(s):
    print(f"Running strategy {s}")


def launch(strats):
    for s in strats:
        Process(target=run_strategy, args=(s,)).start()
