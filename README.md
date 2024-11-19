# **Fruit Ripeness Detection Using IoT and Image Recognition**

This repository contains the implementation of a fruit ripeness detection system that leverages IoT sensors and advanced image recognition models (VGG16 and MobileNetV2) to determine the optimal time for harvesting fruits. The system is designed for novelty and achieves high accuracy through the integration of environmental sensors and machine learning.

---

## **Project Description**

This project uses a combination of:
- **IoT Sensors**: To measure environmental and gas parameters (e.g., temperature, CO2 levels, ethylene presence) affecting fruit ripeness.
- **Image Recognition**: Leveraging pre-trained models (VGG16 and MobileNetV2) for accurate classification of fruit ripeness based on visual characteristics.
- **Raspberry Pi Integration**: Serving as the primary controller for processing sensor data and executing image recognition models.

---

## **Key Features**
1. **Non-contact Temperature Measurement**: Detect ripeness through surface temperature monitoring using the MLX90614 IR sensor.
2. **Gas Analysis**: Detect ethylene and CO2 levels with MQ-2 or MH-Z19B gas sensors to determine fruit's biochemical changes.
3. **Image Recognition Models**:
   - **VGG16**: For high-accuracy feature extraction and classification.
   - **MobileNetV2**: For lightweight, real-time classification tasks.
4. **IoT Connectivity**: Wireless data transmission and monitoring using the ESP8266 module.
5. **Portable Power Solution**: Rechargeable battery integration for field use.

---

## **How It Works**
1. **Data Collection**: Sensors capture temperature, gas concentration, and images of the fruit.
2. **Preprocessing**:
   - Sensor data is normalized and sent to the Raspberry Pi.
   - Captured images are resized and preprocessed for input into the image recognition models.
3. **Model Inference**:
   - VGG16 and MobileNetV2 classify the fruit's ripeness stage (e.g., unripe, ripe, overripe).
4. **Data Transmission**: Results are sent to a cloud platform via the ESP8266 for visualization or stored locally.
5. **Decision Making**: Combines sensor and model outputs to determine the optimal harvesting time.

---

## **Technologies Used**
- **Hardware**:
  - Raspberry Pi 3 Model B
  - Raspberry Pi Camera Module v1.3
  - MLX90614 IR Temperature Sensor
  - MQ-2 Gas Sensor / MH-Z19B CO2 Sensor
  - TCS3200 / APDS9960 Color Sensors
  - ESP8266 Wi-Fi Module
- **Software**:
  - Python 3.8+
  - TensorFlow / Keras
  - OpenCV for image preprocessing
  - Matplotlib and Pandas for data analysis
- **Machine Learning Models**:
  - VGG16
  - MobileNetV2

---

## **Data Flow**
1. Sensor Inputs:
   - **Temperature**: Measured using MLX90614.
   - **Gas Levels**: Ethylene and CO2 detected by MQ-2 or MH-Z19B sensors.
   - **Color**: Analyzed with APDS9960 or TCS3200.
2. Image Recognition:
   - Captured by Raspberry Pi Camera.
   - Processed by pre-trained models for ripeness classification.
3. Output:
   - Sent to a dashboard or stored in CSV format for later analysis.

---

## **Collaborators**
- **Collaborator 1**: [Name] - Lead Hardware Developer
- **Collaborator 2**: [Name] - Machine Learning Engineer
- **Collaborator 3**: [Name] - IoT Specialist
- **Collaborator 4**: [Name] - Software Integrator
- **Collaborator 5**: [Name] - Data Analyst

---

## **Future Enhancements**
1. Integration with cloud platforms for real-time monitoring and notifications.
2. Deployment of models on edge devices for faster in-field predictions.
3. Expansion of the dataset to include more fruit types and environmental variations.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
