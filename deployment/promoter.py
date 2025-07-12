Below is a Python script that promotes safe modules from a staging directory to a live system directory and logs the changes. This script assumes that you have a staging directory where modules are tested and a live directory where approved modules are placed for production use. It also assumes that each module is a file.

```python
import os
import shutil
import logging
from datetime import datetime

def setup_logging():
    logging.basicConfig(filename='promotion_log.log', level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')

def promote_modules(staging_dir, live_dir):
    """
    Promotes safe modules from the staging directory to the live directory.
    
    Args:
    staging_dir (str): The directory containing the tested modules ready for promotion.
    live_dir (str): The directory where the safe modules will be moved for production use.
    """
    # Ensure directories exist
    if not os.path.exists(staging_dir):
        logging.error(f"Staging directory {staging_dir} does not exist.")
        return
    if not os.path.exists(live_dir):
        os.makedirs(live_dir)
        logging.info(f"Created live directory {live_dir}.")

    # List all files in the staging directory
    modules = os.listdir(staging_dir)
    for module in modules:
        staging_module_path = os.path.join(staging_dir, module)
        live_module_path = os.path.join(live_dir, module)

        # Move each module from staging to live
        try:
            shutil.move(staging_module_path, live_module_path)
            logging.info(f"Promoted {module} from {staging_dir} to {live_dir}.")
        except Exception as e:
            logging.error(f"Failed to promote {module} from {staging_dir} to {live_dir}. Error: {e}")

if __name__ == "__main__":
    setup_logging()
    staging_directory = 'path/to/staging'
    live_directory = 'path/to/live'
    promote_modules(staging_directory, live_directory)
```

This script uses Python's built-in `shutil` and `os` modules to handle file operations and `logging` to log the operations. Adjust the `staging_directory` and `live_directory` paths to match your directory structure. The script logs all operations, including errors, which helps in tracking the changes and troubleshooting if needed.