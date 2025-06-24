# 🌱 Smart Soil Monitoring System

A final-year engineering project combining **IoT (Raspberry Pi Pico)** and **Machine Learning (Mobile App)** for real-time soil condition monitoring and prediction.

---

## 🔧 Hardware Component (Raspberry Pi Pico)

This project uses a combination of sensors connected to the Raspberry Pi Pico to monitor environmental and soil parameters:

- **Soil Moisture Sensor**
- **DHT11 Temperature & Humidity Sensor**
- **LDR Light Sensor**

All sensor scripts are located inside the [`Hardware/`](./Hardware/) folder.

> These scripts collect live data and transmit it to the mobile app for monitoring and prediction.

---

## 💻 Software Component (ML App)

A mobile app was developed to receive sensor data and make predictions using a trained machine learning model.

- Model training and evaluation are handled in [`SoilMonitor.ipynb`](./Software/SoilMonitor.ipynb)
- The trained model is provided inside [`Varieties of Soil.zip`](./Software/Varieties%20of%20Soil.zip)
- The mobile app source code is **not included** in this repository. However, a working demonstration is shown in the video below.

---

## 📱 App Interface

![Soil Monitor App](https://github.com/user-attachments/assets/f488958f-4498-40bb-b22e-27a99fd33dd2)

---

## 📽️ Demo Video

🎥 **Watch the full demo here:**  
[https://youtu.be/GBO5wUBHAj4](https://youtu.be/GBO5wUBHAj4)

---

## 🖼️ Visuals

| Circuit Diagram | App Interface |
|-----------------|----------------|
| ![Circuit Diagram](https://github.com/user-attachments/assets/112bac72-8571-49c5-a52c-886eb62c75e9) | ![App Interface](https://github.com/user-attachments/assets/c48e4985-830b-4291-acbf-1e708117e7bc) |

---

## 📊 Sample Outputs

Here are some example outputs captured during project testing and deployment:

| Database View (Sensor Data Stored) | App Output (Live Sensor Display) |
|------------------------------------|----------------------------------|
| ![Database](https://github.com/user-attachments/assets/c1db7d71-9335-4241-90bc-fe0d839fb68a) | ![Mobile App](https://github.com/user-attachments/assets/c86b71fc-6d3b-4a0d-9810-8027593a1e58) |

### ✅ Model Prediction Score Output

![Prediction Output](https://github.com/user-attachments/assets/75750c75-20de-449e-8543-bfadeacbb8ae)

---

## 🚀 How to Run the Project

1. **Connect the sensors** to the Raspberry Pi Pico as shown in the circuit diagram.
2. Upload the respective `.py` sensor scripts from the [`Hardware/`](./Hardware/) folder using **Thonny IDE**.
3. Launch the **mobile application** (not included in this repository):
   - It receives sensor readings via USB, serial, Bluetooth, or WiFi (depending on your setup)
   - Uses the trained ML model to predict soil type or condition
4. To test the model externally:
   - Unzip [`Varieties of Soil.zip`](./Software/Varieties%20of%20Soil.zip)
   - Load the model into your Python/Flutter/Android interface for testing or integration

---

## 🧠 Algorithm & Model Summary

![Algorithm Diagram](https://github.com/user-attachments/assets/87329fe1-b6dd-464d-a1d4-4ea327d136d3)

**Machine Learning Details:**

- **Algorithm:** Convolutional Neural Network (CNN) for image-based soil classification
- **Input Features:** Moisture %, Temperature (°C), Humidity %, Light Intensity
- **Output Classes:** Sandy, Clayey, Alluvium, Black, and other soil types
- **Dataset:** Custom-collected or UCI-based soil dataset
- **Achieved Accuracy:** **95.79%**

> The model was trained using TensorFlow and exported as a `.tflite` file for use in mobile inference.

---

## 📄 Project Highlights

- ✅ Real-time sensor data acquisition via Raspberry Pi Pico
- ✅ ML-powered prediction integrated into a mobile app
- ✅ Farmer-friendly interface for real-world use
- ✅ Affordable and scalable smart agriculture solution

---

## 👨‍💻 Developed By

- **Arpan Biswas**
- **Subhrajyoti Mandal**
- **Shibam Mishra**

**Department of Electronics and Telecommunication Engineering**  
**Hooghly Engineering and Technology College**
**Final Year Project – 2025**

---

## 📝 License

This project is licensed under the [MIT License](./LICENSE).
