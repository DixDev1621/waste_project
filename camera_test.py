import os, time, csv, cv2, numpy as np, serial, json
from tensorflow.keras.models import load_model

# ---------- CONFIG ----------
MODEL_PATH = "D:/waste_project/models/waste_model_transfer_finetuned2.h5"
TRAIN_DIR = "D:/waste_project/data/train"   # used to infer class label order
CONF_THRESHOLD = 0.70                       # show prediction only if confidence > 70%
LOG_CSV = "D:/waste_project/logs/predictions.csv"
ARDUINO_PORT = "COM3"                       # 🔴 Change this to your Arduino port
BAUD_RATE = 9600
# ----------------------------

# Connect to Arduino
try:
    arduino = serial.Serial(ARDUINO_PORT, BAUD_RATE)
    time.sleep(2)
    print(f"✅ Connected to Arduino on {ARDUINO_PORT}")
except Exception as e:
    arduino = None
    print("⚠ Could not connect to Arduino:", e)

# Load class labels
if os.path.exists("D:/waste_project/models/class_indices.json"):
    with open("D:/waste_project/models/class_indices.json", "r") as f:
        class_map = json.load(f)
    class_labels = [None]*len(class_map)
    for name, idx in class_map.items():
        class_labels[int(idx)] = name
else:
    class_labels = sorted([d for d in os.listdir(TRAIN_DIR) if os.path.isdir(os.path.join(TRAIN_DIR,d))])

print("Using labels (in order):", class_labels)

# Load model
model = load_model(MODEL_PATH)
print("✅ Loaded model:", MODEL_PATH)

# Ensure log folder exists
os.makedirs(os.path.dirname(LOG_CSV), exist_ok=True)
if not os.path.exists(LOG_CSV):
    with open(LOG_CSV, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "pred_label", "confidence"])

# Open camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise SystemExit("❌ Cannot open camera (check camera index).")

print("📸 Camera started. Place object in front of webcam. Press 'q' to quit.")

# Get frame size
ret, frame = cap.read()
h, w = frame.shape[:2]
size = min(h, w) // 3   # dynamic crop size

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Center crop region
    center_x, center_y = w//2, h//2
    x1, y1 = max(0, center_x-size), max(0, center_y-size)
    x2, y2 = min(w, center_x+size), min(h, center_y+size)
    crop = frame[y1:y2, x1:x2]

    # Preprocess
    img = cv2.resize(crop, (128,128))
    arr = np.expand_dims(img.astype("float32")/255.0, axis=0)

    # Predict
    preds = model.predict(arr, verbose=0)
    pred_idx = int(np.argmax(preds, axis=1)[0])
    pred_label = class_labels[pred_idx]
    confidence = float(np.max(preds))

    # Show result
    if confidence >= CONF_THRESHOLD:
        text = f"{pred_label} ({confidence*100:.1f}%)"
        color = (0,200,0)
    else:
        text = "Not sure"
        color = (0,165,255)

    # Draw box + label
    cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0), 2)
    cv2.putText(frame, text, (10,40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.imshow("Waste Classification (press q to quit)", frame)

    # Log predictions
    if confidence >= CONF_THRESHOLD:
        with open(LOG_CSV, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), pred_label, f"{confidence:.4f}"])

        # Send to Arduino
        if arduino:
            if pred_label.lower() == "recyclable":
                arduino.write(b"recyclable\n")
            elif pred_label.lower() == "hazardous":
                arduino.write(b"hazardous\n")
            else:
                # For biodegradable, no action
                arduino.write(b"none\n")

    # Quit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
if arduino:
    arduino.close()
print("🟢 Camera stopped. Log saved to:", LOG_CSV)