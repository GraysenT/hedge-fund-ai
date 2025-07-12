import os
import openai
import json
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load OpenAI API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# ✅ Build files into current directory structure
TARGET_DIR = "."  # Do NOT nest again

# ✅ Points to your master queue of 1,100+ modules
QUEUE_FILE = "autonomy/module_queue.json"

# Number of modules to generate at once
MAX_WORKERS = 10

def generate_file(prompt, filename):
    # Strip any redundant prefix if included in queue
    clean_filename = filename.replace("hedge_fund_ai_package/", "").lstrip("/")
    full_path = os.path.join(TARGET_DIR, clean_filename)

    # ✅ Skip if file already exists
    if os.path.exists(full_path):
        print(f"⏩ Skipping {clean_filename} (already exists)")
        return

    print(f"🧠 Generating: {clean_filename}")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            temperature=0.2,
            messages=[
                {"role": "system", "content": "You are an expert AI engineer. Output full working Python code only."},
                {"role": "user", "content": prompt},
            ]
        )
        code = response['choices'][0]['message']['content']

        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(code.strip())

        print(f"✅ Saved: {full_path}")
    except Exception as e:
        print(f"❌ Error generating {clean_filename}: {e}")

def load_queue():
    try:
        with open(QUEUE_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Failed to load queue: {e}")
        return {}

def build_all_parallel():
    module_queue = load_queue()
    print(f"\n🚀 Starting parallel build: {len(module_queue)} modules...\n")

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [
            executor.submit(generate_file, prompt, filename)
            for filename, prompt in module_queue.items()
        ]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"⚠️ Worker error: {e}")

    print("\n✅ Build process complete.")

if __name__ == "__main__":
    build_all_parallel()