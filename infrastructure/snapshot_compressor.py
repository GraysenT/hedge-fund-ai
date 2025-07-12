Below is a Python script that compresses snapshots (directories) into deployable seeds or backups using the `zipfile` module. This script will take a directory path as input and create a compressed ZIP file as output. This can be used for creating backups or deployable seeds of project directories, configuration settings, or any other type of file collections.

```python
import os
import zipfile
from datetime import datetime

def compress_directory_to_zip(source_dir, output_dir=None, zip_name=None):
    """
    Compresses the specified directory into a ZIP file.

    :param source_dir: Path to the directory to be compressed.
    :param output_dir: Directory where the ZIP file will be saved. If None, uses the source directory.
    :param zip_name: Name of the output ZIP file. If None, a name based on the current date and time is used.
    :return: Path to the created ZIP file.
    """
    if not os.path.isdir(source_dir):
        raise ValueError("The source directory does not exist")

    if output_dir is None:
        output_dir = source_dir

    if zip_name is None:
        zip_name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '_backup.zip'
    else:
        zip_name = zip_name + '.zip'

    zip_path = os.path.join(output_dir, zip_name)

    # Creating the zip file
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=source_dir)
                zipf.write(file_path, arcname)

    return zip_path

# Example usage:
if __name__ == "__main__":
    source_directory = input("Enter the path to the directory to compress: ")
    output_directory = input("Enter the output directory for the ZIP file (optional, press enter to use source directory): ")
    zip_file_name = input("Enter a name for the ZIP file (optional, press enter to use default naming): ")

    # Compress the directory
    try:
        zip_file_path = compress_directory_to_zip(source_directory, output_directory if output_directory else None, zip_file_name if zip_file_name else None)
        print(f"Directory compressed successfully into: {zip_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
```

This script:
- Compresses all files and subdirectories within the specified directory.
- Allows optional specification of the output directory and the name of the ZIP file.
- Uses the current date and time to name the ZIP file if no name is provided.
- Handles exceptions and provides user feedback.