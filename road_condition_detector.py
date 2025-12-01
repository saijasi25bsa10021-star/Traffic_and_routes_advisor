
import os
import random
import os
import random

def detect_road_condition():
    base_dir = "dataset_traffic"
    processed_dir = os.path.join(base_dir, "processed/images")

    # NEW: Check the processed folder instead of IDD_RESIZED
    images = [f for f in os.listdir(processed_dir)
              if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    if not images:
        print("❌ No images found in processed/images! Cannot detect road condition.")
        return "Unknown"

    # Pick a random image
    image_path = os.path.join(processed_dir, random.choice(images))
    print(f"✔ Using image for detection: {image_path}")

    # Fake classification (you can improve later)
    conditions = ["Clear Road", "Moderate Traffic", "Heavy Traffic", "Obstacle Ahead"]
    detected = random.choice(conditions)

    return detected


