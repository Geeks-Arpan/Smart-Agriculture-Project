# 🌱 Smart Soil Monitoring System

A Final Year Engineering Project combining **IoT (Raspberry Pi Pico)** and **Machine Learning (Mobile App)** for real-time soil monitoring and prediction.

---

## 🔧 Hardware Part (Raspberry Pi Pico)

This project uses several sensors connected to a Raspberry Pi Pico:

- **Soil Moisture Sensor**
- **DHT11 Temperature & Humidity Sensor**
- **LDR Light Sensor**

Each sensor has its script inside the `Hardware/` folder.

> These scripts read sensor data and send it for processing or display on the app.

---

## 💻 Software Part (ML App)

- A mobile app was developed to interact with the Raspberry Pi Pico and make predictions using a **trained machine learning model**.
The trained model is contained in the file`Varieties of Soil.zip` in the `Software/` folder.
- The file **SoilMonitor.ipynb`** defines and trains the ML model.
- The app source code is not included in this repository, but the model and demonstration are available.

---

## 📱 App Interface (ML App)

<img src="images/soil_monitor_app.png" alt="App Interface" width="400"/>

---

## 📽️ Demo Video

🎥 **Watch the full demo here**:  
[![Watch on YouTube](https://img.youtube.com/vi/VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID_HERE)

> Replace `VIDEO_ID_HERE` with your actual YouTube video ID.

---

## 🖼️ Visuals

| Circuit Diagram           | App Interface              |
|---------------------------|----------------------------|
| ![Circuit](images/circuit_diagram.png) | ![App](images/app_interface.png) |

---

## 🚀 How to Run the Project

1. **Connect all sensors** to the Raspberry Pi Pico according to the circuit diagram.
2. Upload the appropriate sensor code from the `Hardware/` folder.
3. Launch the mobile app (not included here) to:
   - Collect real-time sensor data
   - Make predictions using the trained ML model
4. Optionally, host or integrate the model using the zipped file provided.

---

## 📄 Project Summary

- ✅ Real-time data collection via Raspberry Pi Pico and sensors
- ✅ ML model trained to identify soil conditions
- ✅ Mobile app for real-time interaction
- ✅ Cost-effective and scalable solution for smart farming

---

## 👨‍💻 Developed By

- **Arpan Biswas**
- **Subhrajyoti Mandal**
- **Shibam Mishra**

Department of Electronics and Telecommunication Engineering  
**Hooghly Engineering and Technology College**  
**Final Year Project – 2025**

---
