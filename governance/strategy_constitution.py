```python
# Define a class to manage the rights, limits, and responsibilities of modules
class ModuleManager:
    def __init__(self):
        # Define the rights, limits, and responsibilities for each module
        self.modules = {
            "authentication": {
                "rights": ["validate_user", "create_session"],
                "limits": ["max_login_attempts: 5"],
                "responsibilities": ["user_identity_verification", "session_security"]
            },
            "data_processing": {
                "rights": ["read_data", "process_data", "write_data"],
                "limits": ["max_data_size: 1000MB"],
                "responsibilities": ["ensure_data_integrity", "optimize_data_processing"]
            },
            "user_management": {
                "rights": ["create_user", "delete_user", "update_user"],
                "limits": ["max_users: 10000"],
                "responsibilities": ["manage_user_accounts", "ensure_user_privacy"]
            },
            "reporting": {
                "rights": ["generate_reports", "access_reports"],
                "limits": ["max_reports_per_day: 20"],
                "responsibilities": ["accurate_reporting", "timely_report_generation"]
            }
        }

    def get_module_info(self, module_name):
        # Return the information of the specified module
        return self.modules.get(module_name, "Module not found")

# Example usage
module_manager = ModuleManager()
authentication_info = module_manager.get_module_info("authentication")
print(authentication_info)
```