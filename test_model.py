import os
import json
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# --- Paths (change only if you used different folders) ---
MODEL_PATH = "D:/waste_project/models/waste_model.h5"
CLASS_MAP_PATH = "D:/waste_project/models/class_indices.json"   # optional (if saved during training)
TRAIN_DIR = "D:/waste_project/data/train"  # used to infer class order if no json
TEST_DIR = "D:/waste_project/data/test"

# --- Load model ---
model = load_model(MODEL_PATH)

# --- Get class names in correct order ---
if os.path.exists(CLASS_MAP_PATH):
    # If you saved mapping {class_name: index} during training, load and invert it
    with open(CLASS_MAP_PATH, "r") as f:
        class_map = json.load(f)            # e.g. {"biodegradable": 0, "recyclable": 1, ...}
    # invert to get list by index
    class_names = [None] * len(class_map)
    for name, idx in class_map.items():
        class_names[int(idx)] = name
    print("Loaded class mapping from", CLASS_MAP_PATH)
else:
    # Fallback: infer from TRAIN_DIR subfolders (flow_from_directory uses sorted folder names)
    if not os.path.exists(TRAIN_DIR):
        raise SystemExit(f"Cannot find {TRAIN_DIR}. Create it or save class_indices.json.")
    class_names = sorted([d for d in os.listdir(TRAIN_DIR) if os.path.isdir(os.path.join(TRAIN_DIR, d))])
    print("Inferred class order from train folder (alphabetical):", class_names)

# --- Sanity check ---
num_model_outputs = model.output_shape[-1]
if num_model_outputs != len(class_names):
    raise SystemExit(f"Model outputs {num_model_outputs} probabilities but there are {len(class_names)} class names. "
                     "Fix class mapping or retrain with saved class_indices.json.")

# --- Walk test folder and predict ---
total = 0
correct = 0

for true_label in sorted(os.listdir(TEST_DIR)):
    true_folder = os.path.join(TEST_DIR, true_label)
    if not os.path.isdir(true_folder):
        continue

    for fname in sorted(os.listdir(true_folder)):
        if not fname.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        img_path = os.path.join(true_folder, fname)
        try:
            img = image.load_img(img_path, target_size=(128, 128))
        except Exception as e:
            print("Skipping (cannot open):", img_path, "->", e)
            continue

        arr = image.img_to_array(img)
        arr = np.expand_dims(arr, axis=0) / 255.0

        preds = model.predict(arr, verbose=0)
        pred_idx = int(np.argmax(preds, axis=1)[0])
        pred_label = class_names[pred_idx]

        total += 1
        if pred_label == true_label:
            correct += 1

        print(f"{true_label}/{fname}  -> predicted: {pred_label}")

# --- Summary ---
if total == 0:
    print("No test images found. Check", TEST_DIR)
else:
    acc = correct / total * 100.0
    print(f"\nTotal images: {total}")
    print(f"Correct predictions: {correct}")
    print(f"Accuracy: {acc:.2f}%")
