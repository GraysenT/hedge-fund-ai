import os
import openai
import time
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Directory to write files to
TARGET_DIR = "hedge_fund_ai_package"

# 🔁 SAMPLE MODULE QUEUE (expand this with your full system)
ALL_MODULES = {
    "daemon/evolution_daemon.py": "Create a Python module that runs evolve.py and runloop.py in the background with logging, subprocess handling, and fault recovery.",
    "auto_coder/code_writer.py": "Module that generates Python files from strategy goals. Include generate_new_module(goal: str) that returns Python code.",
    "simulation/safety_tester.py": "Test generated Python code for safety, imports, logic, and performance. Include test_module(code: str) -> dict.",
    "deployment/promoter.py": "Move tested code into production folders and log promotion. Include GitHub commit stub.",
    "dashboards/meta_growth.py": "Streamlit dashboard showing files built, lines of code added, and evolution logs.",
    "meta/self_identity.py": "Track the system's evolving structure, traits, and internal growth history as a self-reflective identity module.",
    "reinforcement/inner_dialogue.py": "Internal self-talk logic module that lets the system resolve conflicts between strategies or modules using weighted reasoning.",
    "meta/purpose_engine.py": "Assign long-term mission and goal logic to the program. Let it evolve what success means over time.",
    "meta/self_defense.py": "Automatically detect and block logic that could destabilize the system or destroy alpha.",
}

# Function to call OpenAI API and write file
def generate_file(prompt, filename):
    print(f"🧠 Generating: {filename}")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            temperature=0.3,
            messages=[
                {"role": "system", "content": "You are an expert AI code generator. Only return full working Python code."},
                {"role": "user", "content": prompt},
            ]
        )
        code = response['choices'][0]['message']['content']

        full_path = os.path.join(TARGET_DIR, filename)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, "w") as f:
            f.write(code.strip())

        print(f"✅ Saved: {full_path}")
    except Exception as e:
        print(f"❌ Error generating {filename}: {e}")

# Threaded parallel builder
def build_all_modules_parallel():
    print(f"\n🚀 Starting FULL SYSTEM BUILD ({len(ALL_MODULES)} modules in parallel)...\n")
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for filename, prompt in ALL_MODULES.items():
            futures.append(executor.submit(generate_file, prompt, filename))
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"❌ Threaded task failed: {e}")
    print("\n✅ All modules completed.")

# Entrypoint
def main():
    print("🔁 Autonomous OpenAI Builder (Parallel Mode)")
    build_all_modules_parallel()

if __name__ == "__main__":
    main()