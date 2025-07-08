from monitor.deployment_validator import validate_deployment
from monitor.deployment_lock import is_deployment_locked

def show_deployment_status_dashboard():
    print("\n📦 Deployment Status Dashboard")
    valid = validate_deployment()
    locked = is_deployment_locked()
    print(f"\n🔐 Deployment Lock: {'ACTIVE' if locked else 'INACTIVE'}")
    print(f"🧠 System Integrity Score: {'100%' if valid else 'INCOMPLETE'}")

if __name__ == "__main__":
    show_deployment_status_dashboard()