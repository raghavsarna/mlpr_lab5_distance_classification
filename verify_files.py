import os
import cv2

required_files = ["Plaksha_Faculty.jpg", "Dr_Shashi_Tharoor.jpg", "Lab 5-Spring 2025 (1).ipynb"]

missing_files = [file for file in required_files if not os.path.exists(file)]
if missing_files:
    print("Missing files:", missing_files)
else:
    print("All required files are present.")

for image_file in ["Plaksha_Faculty.jpg", "Dr_Shashi_Tharoor.jpg"]:
    img = cv2.imread(image_file)
    if img is None:
        print(f"Error loading {image_file}")
    else:
        print(f"Successfully loaded {image_file} (Dimensions: {img.shape})")

print("File verification complete.")
