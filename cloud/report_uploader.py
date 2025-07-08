import subprocess
from pathlib import Path

REPORT_DIR = Path("reports/generated")
REMOTE = "Cloud_Trading:/hedge_fund_ai/reports/"

def upload_reports():
    print("☁️ Uploading investor reports to cloud...")
    result = subprocess.run([
        "rclone", "copy", str(REPORT_DIR), REMOTE, "--update", "-v"
    ], capture_output=True)
    print(result.stdout.decode())
    print("✅ Report upload complete.")