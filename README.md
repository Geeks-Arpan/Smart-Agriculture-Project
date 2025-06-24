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

![Prediction Output](https://github.com/user-)
