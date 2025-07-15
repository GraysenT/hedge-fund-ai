def start_dashboard():
    import subprocess
    import os
    path = os.path.abspath("dashboard/dashboard_app.py")
    print("📊 Launching dashboard at http://localhost:8500")
    subprocess.Popen(["streamlit", "run", path, "--server.port=8500"])
