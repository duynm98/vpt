from PIL import Image
import os

# 📂 Folder paths
input_folder = "."  # folder with original images
output_folder = "resized_images"  # folder to save resized images

# 📐 Target size
TARGET_WIDTH = 600
TARGET_HEIGHT = 800

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Supported image formats
supported_formats = (".jpg", ".jpeg", ".png", ".webp")

for filename in os.listdir(input_folder):
    if filename.lower().endswith(supported_formats):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with Image.open(input_path) as img:
            # Resize image
            resized_img = img.resize((TARGET_WIDTH, TARGET_HEIGHT), Image.LANCZOS)

            # Save resized image
            resized_img.save(output_path, quality=95)

        print(f"Resized: {filename}")

print("✅ All images resized successfully!")
