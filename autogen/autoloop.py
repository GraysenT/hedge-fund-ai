import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from autogen.phase_builder import build_next_phase
from autogen.queue_reader import get_next_phase, mark_phase_complete

def run_autoloop():
    while True:
        phase = get_next_phase()
        if not phase:
            print("✅ All Ultra-Frontier Phases are now complete.")
            break
        build_next_phase()
        mark_phase_complete(phase["id"])

if __name__ == "__main__":
    run_autoloop()