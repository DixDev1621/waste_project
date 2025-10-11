from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import os, serial, time, base64
from io import BytesIO
from PIL import Image

# ---------------- CONFIG ----------------
MODEL_PATH = "D:/waste_project/models/waste_model_transfer_finetuned2.h5"
TRAIN_DIR = "D:/waste_project/data/train"
ARDUINO_PORT = "COM10"  # Your Arduino port
BAUD_RATE = 9600
# ----------------------------------------

app = Flask(__name__)

# Load model
model = load_model(MODEL_PATH)
print("✅ AI Model Loaded Successfully")

# Try connecting to Arduino safely
arduino = None
try:
    arduino = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=1)
    time.sleep(3)  # Wait Arduino to reset
    print(f"✅ Connected to Arduino on {ARDUINO_PORT}")
except Exception as e:
    print("⚠️ Arduino not connected:", e)

# Load class labels
class_labels = sorted([
    d for d in os.listdir(TRAIN_DIR)
    if os.path.isdir(os.path.join(TRAIN_DIR, d))
])
print("Class labels found:", class_labels)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if 'image' not in data:
            return jsonify({'error': 'No image received'})

        # Decode base64 image
        image_data = data['image'].split(',')[1]
        img = Image.open(BytesIO(base64.b64decode(image_data))).convert("RGB")
        img = img.resize((128, 128))
        img_array = np.expand_dims(np.array(img)/255.0, axis=0)

        # Predict
        preds = model.predict(img_array, verbose=0)
        pred_idx = np.argmax(preds)
        label = class_labels[pred_idx]
        confidence = round(float(np.max(preds) * 100), 2)

        # Send signal to Arduino
        if arduino:
            if label.lower() == "recyclable":
                arduino.write(b"recyclable\n")  # Servo on pin 8
                print("♻ Recyclable bin opened (pin 8)")
            elif label.lower() == "hazardous":
                arduino.write(b"hazardous\n")   # Servo on pin 9
                print("☣ Hazardous bin opened (pin 9)")
            else:
                arduino.write(b"biodegradable\n")  # Arduino will do nothing
                print("🪴 Biodegradable - No servo movement")

        print(f"Predicted: {label} ({confidence}%)")
        return jsonify({'label': label, 'confidence': confidence})

    except Exception as e:
        print("❌ Error during prediction:", e)
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=False)  # ← set debug=False

