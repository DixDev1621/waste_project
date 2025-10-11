import tensorflow as tf

# Path to your trained Keras model
model_path = "D:/waste_project/models/waste_model_transfer_finetuned2.h5"

# Output path for the converted TFLite model
tflite_output = "D:/waste_project/models/waste_model_transfer_finetuned2.tflite"

# Load the model
model = tf.keras.models.load_model(model_path)
print("✅ Model loaded successfully.")

# Convert to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# Optimize for smaller size (optional but recommended)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

tflite_model = converter.convert()

# Save the converted model
with open(tflite_output, "wb") as f:
    f.write(tflite_model)

print("✅ Model successfully converted to TFLite format!")
print(f"📂 Saved at: {tflite_output}")
