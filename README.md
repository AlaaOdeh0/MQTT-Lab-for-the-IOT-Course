# MQTT Lab – Mosquitto + Paho (Python)
**Student ID: 12114470**

This lab demonstrates the use of the **Mosquitto MQTT Broker** with **multiple publishers and subscribers** using the **Paho MQTT Python client**.

The objective is to create a real-time messaging environment with:
- Temperature publisher & subscriber  
- Humidity publisher & subscriber  
- People counter publisher & subscriber  

Each message includes the **student ID (12114470)** as required.

---

#  Features
- Install and configure Mosquitto broker on Windows
- Use Paho MQTT client in Python
- Three publishers (Temperature, Humidity, People Counter)
- Three subscribers (each listens to a specific topic)
- Logs from both PUB and SUB sides
- Includes screenshots 

---

#  Project Structure

mqtt-lab/
│
├── publishers/
│   ├── temp_pub.py
│   ├── humidity_pub.py
│   └── people_pub.py
│
├── subscribers/
│   ├── temp_sub.py
│   ├── humidity_sub.py
│   └── people_sub.py
│
├── screenshots/
│   └── (screenshots)
│
└── README.md


---

#  Installation

### 1. Install Mosquitto Broker
Download for Windows:  
https://mosquitto.org/download/

Make sure to check:
- ✔ Install Windows Service  
- ✔ Add to PATH  

Start broker:
mosquitto -v


### 2. Install Python Dependencies
pip install paho-mqtt
