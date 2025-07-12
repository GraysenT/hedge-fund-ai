import subprocess
import os

def test_module(file_path):
    """
    Run a basic test by attempting to execute the module file.
    Returns True if it runs successfully, False otherwise.
    """
    try:
        result = subprocess.run(
            ["python3", file_path],
            capture_output=True,
            timeout=10
        )
        if result.returncode == 0:
            return True
        else:
            print(f"⚠️ Test failed: {result.stderr.decode()}")
            return False
    except Exception as e:
        print(f"❌ Exception during test: {e}")
        return False
