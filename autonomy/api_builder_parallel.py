import os
import openai
import time
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load OpenAI API Key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

TARGET_DIR = "hedge_fund_ai_package"
MAX_WORKERS = 10  # You can increase up to 20 if not rate-limited

# ✅ FLATTENED MODULE QUEUE FROM 312 PHASES (PARTIAL SAMPLE BELOW)
ALL_MODULES = {
    "daemon/evolution_daemon.py": "Create a daemon that runs evolve.py and runloop.py continuously. Log every cycle and recover from failures safely.",
    "auto_coder/code_writer.py": "Generate new Python modules from internal goals. Include a function generate_new_module(goal: str) that returns code.",
    "simulation/safety_tester.py": "Validate generated code for correctness, import errors, and performance. Return a test report.",
    "deployment/promoter.py": "Promote validated modules into the live folder and optionally log Git/GitHub actions.",
    "dashboards/meta_growth.py": "Build a Streamlit dashboard that shows new files, evolution count, and daily system growth.",

    "meta/self_identity.py": "Track what the system is becoming using versioned memory snapshots and internal role logic.",
    "reinforcement/inner_dialogue.py": "Let the system talk to itself to resolve tradeoffs. Include strategy A vs B reasoning.",
    "meta/purpose_engine.py": "Define long-term goals (alpha, survival, evolution) and tie them to current behavior.",
    "meta/self_defense.py": "Block dangerous modules, unstable signals, or capital-depleting logic autonomously.",

    "feeds/global_context.py": "Pull geopolitical, economic, war, weather data to shape strategy context.",
    "agents/alpha_teacher.py": "Build an agent that learns from past strategies and teaches new agents to avoid errors.",
    "agents/alpha_defender.py": "Protect alpha signals under adversarial market conditions or sabotage.",
    "infrastructure/genesis_seed.py": "Allow system to reboot from memory snapshots and recreate its architecture.",
    "meta/meta_feedback.py": "Score every strategy and module by usefulness, trust, and alpha contribution.",
    "meta/recursive_generator.py": "Build child strategies recursively from surviving ancestors.",
    # 🔁 Add all remaining 700+ module prompts here...
}

def generate_file(prompt, filename):
    print(f"🧠 Generating: {filename}")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            temperature=0.2,
            messages=[
                {"role": "system", "content": "You are an expert AI engineer. Return only full, clean, working Python code for the specified module."},
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

def build_all_parallel():
    print(f"\n🚀 Starting parallel build of {len(ALL_MODULES)} modules...\n")
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(generate_file, prompt, filename) for filename, prompt in ALL_MODULES.items()]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"⚠️ Exception during build: {e}")
    print("\n✅ All modules built and written.")

if __name__ == "__main__":
    build_all_parallel()