# 🌱 Smart Soil Monitoring System

A final-year engineering project combining **IoT (Raspberry Pi Pico)** and **Machine Learning (Mobile App)** for real-time soil condition monitoring and prediction.

---

## 🔧 Hardware Component (Raspberry Pi Pico)

This project integrates multiple sensors with the Raspberry Pi Pico to monitor soil and environmental parameters:

- **Soil Moisture Sensor**
- **DHT11 Temperature & Humidity Sensor**
- **LDR Light Sensor**

All sensor scripts are located inside the [`Hardware/`](./Hardware/) folder.

> These scripts capture real-time sensor data and transmit it for display or further analysis via a connected mobile app.

---

## 💻 Software Component (ML App)

A mobile app is developed to communicate with the Raspberry Pi Pico and perform predictions using a trained machine learning model.

- The model training and evaluation are performed in [`SoilMonitor.ipynb`](./Software/SoilMonitor.ipynb)
- The trained model is provided inside [`Varieties of Soil.zip`](./Software/Varieties%20of%20Soil.zip)
- The mobile app source code is **not included**, but a working demonstration is available in the demo video.

---

## 📱 App Interface
![Soil Monitor App](https://github.com/user-attachments/assets/f488958f-4498-40bb-b22e-27a99fd33dd2)

---

## 📽️ Demo Video

🎥 **Watch the full demo here:**  
https://youtu.be/GBO5wUBHAj4

---

## 🖼️ Visuals

| Circuit Diagram | App Interface |
|-----------------|----------------|
| ![Circuit Diagram](https://github.com/user-attachments/assets/112bac72-8571-49c5-a52c-886eb62c75e9) | ![Soil Monitor App](https://github.com/user-attachments/assets/c48e4985-830b-4291-acbf-1e708117e7bc) |

---

## 📊 Sample Outputs

Here are some sample outputs captured during testing and deployment:

| Database View (Stored Sensor Data) | App Output (Live Sensor Display) |
|------------------------------------|----------------------------------|
| ![Database](https://github.com/user-attachments/assets/c1db7d71-9335-4241-90bc-fe0d839fb68a)
| ![Mobile App](https://github.com/user-attachments/assets/c86b71fc-6d3b-4a0d-9810-8027593a1e58)|

### ✅ Model Prediction Score Output
![Output](https://github.com/user-attachments/assets/75750c75-20de-449e-8543-bfadeacbb8ae)

---

## 🚀 How to Run the Project

1. **Connect the sensors** to the Raspberry Pi Pico as per the circuit diagram.
2. Upload the corresponding `.py` files from the [`Hardware/`](./Hardware/) folder to the Raspberry Pi Pico using **Thonny IDE**.
3. Launch the **mobile application** (not included here):
   - Receives real-time sensor values via serial or Bluetooth/WiFi (depending on your setup)
   - Runs the ML model for real-time soil condition classification or prediction.
4. If you're using the ML model externally:
   - Unzip the file [`Varieties of Soil.zip`](./Software/Varieties%20of%20Soil.zip)
   - Use the model in your Python/Flutter/Android app for inference.

---

## 🧠 Algorithm & Model Summary

![Algo_Model](https://github.com/user-attachments/assets/87329fe1-b6dd-464d-a1d4-4ea327d136d3)

**Machine Learning Algorithm Used:**

- Algorithm: CNN (for image-based analysis)
- Input Features: Moisture %, Temperature (°C), Humidity (%), Light Intensity
- Output Labels: Soil Type (e.g., Sandy, Clayey, Alluvium, Black, etc.)
- Dataset: Custom or UCI dataset used for soil classification
- Accuracy: 95.79%

> You can edit this section to include your training process, model evaluation metrics, or preprocessing steps if applicable.

---

## 📄 Project Highlights

- ✅ Real-time environmental data capture using Pico + sensors
- ✅ Lightweight, on-device ML model for prediction
- ✅ Simple app interface to make it user-friendly for farmers
- ✅ Low-cost and scalable for field deployment

---

## 👨‍💻 Developed By

- **Arpan Biswas**
- **Subhrajyoti Mandal**
- **Shibam Mishra**

**Department of Electronics and Telecommunication Engineering**  
Hooghly Engineering and Technology College  
**Final Year Project – 2025**

---

## 📝 License

This project is licensed under the [MIT License](./LICENSE).
