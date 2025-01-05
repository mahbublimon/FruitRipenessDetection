import argparse
import os
import cv2
import joblib
import numpy as np

def load_model(model_path):
    """Load the trained model from the specified path."""
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    model = joblib.load(model_path)
    return model

def preprocess_image(image_path, image_size=(224, 224)):
    """Preprocess the input image for classification."""
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image file not found at {image_path}")
    
    # Resize the image
    image = cv2.resize(image, image_size)
    
    # Normalize the image
    image = image / 255.0
    
    # Convert to the format the model expects
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

def classify_image(model, image):
    """Classify the image using the trained model."""
    prediction = model.predict(image)
    class_label = np.argmax(prediction)  # Get the index of the highest score
    class_confidence = np.max(prediction)  # Get the confidence score
    return class_label, class_confidence

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Classify an image for ripeness.")
    parser.add_argument("--image", required=True, help="Path to the image file to classify.")
    args = parser.parse_args()

    # Paths and parameters
    model_path = "models/ripeness_model.pkl"
    image_path = args.image

    try:
        # Load the trained model
        print("[INFO] Loading model...")
        model = load_model(model_path)

        # Preprocess the input image
        print("[INFO] Preprocessing image...")
        image = preprocess_image(image_path)

        # Classify the image
        print("[INFO] Classifying image...")
        class_label, confidence = classify_image(model, image)

        # Map class label to human-readable names
        class_mapping = {0: "Unripe", 1: "Ripe", 2: "Overripe"}
        label_name = class_mapping.get(class_label, "Unknown")

        print(f"[RESULT] The fruit is classified as: {label_name} with confidence: {confidence:.2f}")

    except Exception as e:
        print(f"[ERROR] {str(e)}")