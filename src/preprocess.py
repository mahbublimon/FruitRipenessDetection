import cv2
import numpy as np

def preprocess_image(image_path):
    # Load the image
    img = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Resize image to a consistent size
    resized = cv2.resize(gray, (100, 100))
    
    # Normalize pixel values
    normalized = resized / 255.0
    
    return normalized