import os

def remove_files(input_dir):
    for root, _, files in os.walk(input_dir):
        for filename in files:
            if filename.lower().endswith(".heic"):
                file_path = os.path.join(root, filename)
                os.remove(file_path)
                print(f"Removed: {file_path}")
            elif "_v2" not in filename and filename.lower().endswith(".png"):
                file_path = os.path.join(root, filename)
                os.remove(file_path)
                print(f"Removed: {file_path}")

# Specify input directory
input_dir = "./"

# Remove files in the input directory and subdirectories
remove_files(input_dir)
