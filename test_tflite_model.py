import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.preprocessing import image

# Paths
tflite_model_path = "D:/waste_project/models/waste_model_transfer_finetuned2.tflite"
test_folder = "D:/waste_project/data/test"
class_names = ['biodegradable', 'hazardous', 'recyclable']

# Load TFLite model
interpreter = tf.lite.Interpreter(model_path=tflite_model_path)
interpreter.allocate_tensors()
print("✅ TFLite model loaded successfully!")

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Function to predict single image
def predict_image(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    interpreter.set_tensor(input_details[0]['index'], img_array.astype(np.float32))
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    predicted_class = class_names[np.argmax(output_data)]
    return predicted_class

# Test with few images
sample_folder = os.path.join(test_folder, "biodegradable")  # You can change to other folders
sample_images = os.listdir(sample_folder)[:10]

for img_file in sample_images:
    img_path = os.path.join(sample_folder, img_file)
    result = predict_image(img_path)
    print(f"🖼️ {img_file} → Predicted: {result}")
