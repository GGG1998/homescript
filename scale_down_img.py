from PIL import Image
import os

def scale_image(input_path, max_dimension=1600, max_size_mb=5):
    with Image.open(input_path) as img:
        # Check if image exceeds max size
        if os.path.getsize(input_path) > max_size_mb * 1024 * 1024:
            # Resize image while keeping aspect ratio
            img.thumbnail((max_dimension, max_dimension))
            output_path = os.path.splitext(input_path)[0] + "_v2" + os.path.splitext(input_path)[1]
            img.save(output_path)
            print(f"Image scaled and saved to: {output_path}")
        else:
            print("Image does not exceed 5MB, no scaling needed.")

# Specify input directory
input_dir = "./"

# Process images in input directory and subdirectories
for root, _, files in os.walk(input_dir):
    for filename in files:
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            input_path = os.path.join(root, filename)
            scale_image(input_path)
