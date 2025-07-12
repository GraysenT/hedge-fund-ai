import os
from datetime import datetime
from utils.file_tools import write_file_safely

AUTO_PUSH_DIR = "auto_generated"

def auto_push_code(code_str: str):
    os.makedirs(AUTO_PUSH_DIR, exist_ok=True)
    filename = f"{AUTO_PUSH_DIR}/gpt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
    write_file_safely(filename, code_str)
    print(f"✅ Code auto-pushed to: {filename}")