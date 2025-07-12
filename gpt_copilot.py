import os
import json
import requests
import threading
from datetime import datetime
from meta.conversational_agent import handle_gpt_prompt
from editor_hooks.vscode_socket import send_code_to_editor, fetch_code_from_editor
from utils.file_tools import write_file_safely, diff_preview

CONVERSATION_LOG = "logs/gpt_conversation_log.json"
AUTO_PUSH_DIR = "auto_generated"

def log_message(role, content):
    os.makedirs(os.path.dirname(CONVERSATION_LOG), exist_ok=True)
    log = []
    if os.path.exists(CONVERSATION_LOG):
        with open(CONVERSATION_LOG, "r") as f:
            log = json.load(f)
    log.append({"timestamp": str(datetime.now()), "role": role, "message": content})
    with open(CONVERSATION_LOG, "w") as f:
        json.dump(log, f, indent=2)

def gpt_copilot_converse(user_input):
    log_message("user", user_input)
    try:
        # Call GPT response generator
        gpt_response = handle_gpt_prompt(user_input)
        log_message("assistant", gpt_response)
        print(f"\n🤖 GPT: {gpt_response}\n")

        # Action Hooks
        if "[FETCH_CODE]" in user_input:
            path = user_input.split("[FETCH_CODE]")[-1].strip()
            code = fetch_code_from_editor(path)
            print(f"📄 Code from {path}:\n{code}")
        elif "[WRITE_CODE]" in user_input:
            path, content = user_input.split("[WRITE_CODE]")[-1].split("::", 1)
            write_file_safely(path.strip(), content.strip())
        elif "[AUTO_PUSH]" in gpt_response:
            filename = f"{AUTO_PUSH_DIR}/gpt_generated_{datetime.now().isoformat()}.py"
            write_file_safely(filename, gpt_response)
            print(f"✅ Auto-pushed to {filename}")

    except Exception as e:
        print(f"❌ GPT Copilot Error: {e}")

def interactive_gpt_loop():
    print("🔁 GPT Co-Pilot Session Started. Type 'exit' to end.")
    while True:
        user_input = input("🧠 You: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            break
        gpt_copilot_converse(user_input)

if __name__ == "__main__":
    interactive_gpt_loop()