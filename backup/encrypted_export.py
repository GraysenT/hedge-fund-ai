import zipfile
import os
from datetime import datetime
from cryptography.fernet import Fernet

# One-time setup (store this securely)
KEY = Fernet.generate_key()
CIPHER = Fernet(KEY)

def zip_and_encrypt():
    out_dir = "backups"
    os.makedirs(out_dir, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    zip_path = f"{out_dir}/snapshot_{date_str}.zip"
    enc_path = f"{zip_path}.enc"

    with zipfile.ZipFile(zip_path, "w") as zipf:
        for folder in ["memory", "strategy_memory", "models"]:
            for root, _, files in os.walk(folder):
                for file in files:
                    zipf.write(os.path.join(root, file))
    print(f"📦 Created ZIP: {zip_path}")

    with open(zip_path, "rb") as f:
        encrypted = CIPHER.encrypt(f.read())
    with open(enc_path, "wb") as f:
        f.write(encrypted)

    print(f"🔐 Encrypted archive saved to: {enc_path}")
    os.remove(zip_path)

if __name__ == "__main__":
    zip_and_encrypt()
    