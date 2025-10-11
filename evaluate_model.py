from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ==========================
# CHANGE MODEL FILE HERE 👇
model_path = "D:/waste_project/models/waste_model_transfer_finetuned2.h5"
# ==========================

test_dir = "D:/waste_project/data/test"

# Load model
model = load_model(model_path)
print(f"✅ Loaded model: {model_path}")

# Data generator for test set
test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(128, 128),
    batch_size=32,
    class_mode='categorical',
    shuffle=False
)

# Predict
Y_pred = model.predict(test_generator, steps=test_generator.samples // test_generator.batch_size + 1)
y_pred = np.argmax(Y_pred, axis=1)

# Classification report
print("📊 Classification Report:")
print(classification_report(test_generator.classes, y_pred, target_names=list(test_generator.class_indices.keys())))

# Confusion matrix
cm = confusion_matrix(test_generator.classes, y_pred)
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=list(test_generator.class_indices.keys()),
            yticklabels=list(test_generator.class_indices.keys()))
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("D:/waste_project/confusion_matrix2.png")
plt.close()
print("✅ Confusion matrix saved as confusion_matrix2.png")

