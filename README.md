# 🌱 Smart Soil Monitoring System

A Final Year Engineering Project that combines **IoT (Raspberry Pi Pico)** and **Machine Learning (Mobile App)** for real-time soil health monitoring and prediction.

---

## 🔧 Hardware (Raspberry Pi Pico)

The system uses multiple sensors connected to a Raspberry Pi Pico:

- 🟤 **Soil Moisture Sensor**
- 🌡️ **DHT11 Temperature & Humidity Sensor**
- 💡 **LDR Light Sensor**

> Individual sensor scripts are located in the `Hardware/` directory.  
> These scripts read sensor data and send it to the mobile app or backend for further processing.

---

## 💻 Software (ML Model + App)

The mobile app interacts with the Raspberry Pi Pico and uses a **trained ML model** for prediction.

- The trained model is provided in the `Software/Varieties of Soil.zip` file.
- Model training and logic are defined in `Software/SoilMonitor.ipynb`.
- The mobile app source code is not included in this repository, but the model and its use are documented.

---

## 📱 App Interface

![Soil Monitor App](https://github.com/user-attachments/assets/f488958f-4498-40bb-b22e-27a99fd33dd2)

---

## 📽️ Demo Video

🎥 **Watch the full project demonstration here**:  
[![Watch on YouTube](https://img.youtube.com/vi/VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID_HERE)

> ℹ️ Replace `VIDEO_ID_HERE` with your actual YouTube video ID.

---

## 🖼️ Visuals

| Circuit Diagram | App Interface |
|-----------------|----------------|
| ![Circuit Diagram](https://github.com/user-attachments/assets/112bac72-8571-49c5-a52c-886eb62c75e9) | ![App UI](https://github.com/user-attachments/assets/c48e4985-830b-4291-acbf-1e708117e7bc) |

---

## 🚀 How to Run the Project

1. **Connect all sensors** to the Raspberry Pi Pico as per the circuit diagram.
2. Upload the corresponding sensor scripts from the `Hardware/` folder.
3. Launch the mobile app (not included here) to:
   - View live sensor data
   - Run predictions using the trained ML model
4. Use the model in `Varieties of Soil.zip` as needed for classification or integration.

---

## ✅ Features

- Real-time data acquisition via Raspberry Pi Pico and sensors
- Machine Learning-based prediction of soil type and condition
- App-based monitoring and interaction
- Scalable and cost-efficient solution for smart agriculture

---

## 👨‍💻 Developed By

- **Arpan Biswas**
- **Subhrajyoti Mandal**
- **Shibam Mishra**

Department of Electronics and Telecommunication Engineering  
**Hooghly Engineering and Technology College**  
Final Year Project – 2025

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

