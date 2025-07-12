import os
from autogen.gpt_writer import generate_phase_modules
from autogen.queue_reader import get_next_phase
from autogen.changelog_writer import write_changelog

PHASE_OUTPUT_DIR = "ultra_frontier_modules"

def build_next_phase():
    phase = get_next_phase()
    if not phase:
        print("✅ All phases complete.")
        return

    print(f"🌀 Building Phase {phase['id']}: {phase['title']}")
    modules = generate_phase_modules(phase)

    os.makedirs(PHASE_OUTPUT_DIR, exist_ok=True)
    for mod in modules:
        path = os.path.join(PHASE_OUTPUT_DIR, mod["path"])
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(mod["code"])
        print(f"✅ Wrote {mod['path']}")

    write_changelog(phase, modules)