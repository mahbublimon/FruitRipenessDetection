import os
import cv2
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import joblib

from preprocess import preprocess_image
from extract_features import extract_color_histogram

# Define paths
train_image_dir = 'dataset/train/images'
train_label_dir = 'dataset/train/labels'

def load_data(image_dir, label_dir):
    features = []
    labels = []
    
    for filename in os.listdir(image_dir):
        if filename.endswith(".jpg"):
            # Get the image path
            image_path = os.path.join(image_dir, filename)
            label_path = os.path.join(label_dir, filename.replace('.jpg', '.txt'))
            
            # Preprocess and extract features
            preprocessed_image = preprocess_image(image_path)
            color_histogram = extract_color_histogram(image_path)
            
            # Combine features
            features.append(color_histogram)
            
            # Read the label (unripe, ripe, overripe)
            with open(label_path, 'r') as label_file:
                label = label_file.readline().strip()
                labels.append(label)
    
    return np.array(features), np.array(labels)

def train_and_save_model():
    # Load training data
    X, y = load_data(train_image_dir, train_label_dir)
    
    # Split data into train and validation sets
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create and train the classifier
    model = SVC(kernel='linear')
    model.fit(X_train, y_train)
    
    # Save the trained model
    joblib.dump(model, 'models/ripeness_model.pkl')

if __name__ == "__main__":
    train_and_save_model()