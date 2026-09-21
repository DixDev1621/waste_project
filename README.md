# ♻️ AI-Powered Smart Waste Segregation System

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Times+New+Roman&weight=700&size=28&duration=3000&pause=1000&color=2563EB&center=true&vCenter=true&width=850&lines=AI-Powered+Smart+Waste+Segregation;Intelligent+Waste+Classification;Automated+Waste+Sorting;Smart+Municipal+Waste+Management" alt="Typing Animation">
</p>

<p align="center">
  <b>AI + Computer Vision + Embedded Systems + Automated Waste Segregation</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AI-Machine%20Learning-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Flask-Web%20Application-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/Arduino-UNO-00979D?style=for-the-badge&logo=arduino">
  <img src="https://img.shields.io/badge/MobileNetV2-Transfer%20Learning-orange?style=for-the-badge">
</p>

---

## 🌍 Overview

The **AI-Powered Smart Waste Segregation System** is an intelligent waste-management solution that combines **Artificial Intelligence, Computer Vision, Flask, Arduino UNO, and servo-controlled hardware** to identify and physically segregate waste.

The current prototype demonstrates the complete workflow:

```text
📷 Camera
      ↓
🧠 AI Waste Classification
      ↓
🌐 Flask Web Application
      ↓
🔌 Serial Communication
      ↓
⚙️ Arduino UNO
      ↓
🔄 Servo Motor
      ↓
🗑️ Waste Bin

The proposed real-world version extends the prototype into a smart municipal garbage collection vehicle, where waste can be identified and segregated during the collection process.

🎯 Problem Statement

Mixed household waste is commonly collected together, creating challenges during later sorting and processing.

Manual sorting can:

Increase sorting effort
Expose workers to mixed waste
Make recyclable recovery more difficult
Increase the complexity of waste processing
Reduce the efficiency of waste management
💡 Proposed Approach

The system aims to move intelligent waste segregation closer to the collection stage.

Instead of depending only on sorting after mixed waste reaches a processing facility, the proposed system identifies and diverts waste into separate compartments.

🚀 Key Features
Feature	Description
🧠 AI Classification	Identifies waste categories using an AI model
📷 Computer Vision	Uses camera-based waste recognition
🌐 Flask Interface	Provides a web interface for prediction
⚙️ Arduino Control	Controls the physical sorting mechanism
🔄 Servo Sorting	Automatically operates the sorting mechanism
🔌 Serial Communication	Python communicates with Arduino
♻️ Waste Segregation	Supports physical waste sorting
🌱 Expandable Architecture	Supports future sensors and categories
🚛 Municipal Integration	Designed for future garbage-truck deployment
🗂️ Waste Categories

The current AI prototype identifies three categories:

♻️ RECYCLABLE

🌱 BIODEGRADABLE

☣️ HAZARDOUS
Prototype Hardware Mapping
♻️ RECYCLABLE
      ↓
   Arduino D8
      ↓
   Servo Motor 1
      ↓
 Recyclable Bin


☣️ HAZARDOUS
      ↓
   Arduino D9
      ↓
   Servo Motor 2
      ↓
 Hazardous Bin


🌱 BIODEGRADABLE
      ↓
   AI Prediction
      ↓
No servo in current prototype
🧠 AI Model

The current prototype uses:

MobileNetV2 + Transfer Learning

The model is trained for three waste classes:

biodegradable
hazardous
recyclable
AI Processing Pipeline
📷 Input Image
      ↓
🖼️ Image Preprocessing
      ↓
🧠 MobileNetV2
      ↓
🔍 Feature Extraction
      ↓
🎯 Classification
      ↓
📊 Prediction + Confidence

The model receives an image from the camera and predicts the corresponding waste category with a confidence value.

🏗️ System Architecture
🔄 Complete Working Flow
⚙️ Prototype Working
1. Waste Input

A waste item is placed in front of the camera.

2. Image Capture

The camera captures the waste image.

3. AI Prediction

The MobileNetV2 model processes the image and predicts:

Recyclable
Biodegradable
Hazardous
4. Flask Processing

The Flask web application displays the predicted category and confidence.

5. Serial Communication

Python sends the corresponding command to Arduino.

Example:

recyclable

or

hazardous
6. Arduino Control

Arduino receives the command and activates the corresponding servo.

7. Physical Sorting

The servo operates the sorting mechanism and directs the waste toward the corresponding bin.

🔌 Arduino Servo Mapping
                ARDUINO UNO

                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
        D8 Servo          D9 Servo
          │                 │
          ▼                 ▼
    ♻️ Recyclable       ☣️ Hazardous
        Bin                 Bin
Serial Commands
recyclable
hazardous
biodegradable
🚛 Proposed Municipal Garbage Truck System

The prototype is designed as a foundation for a larger automated system that can be integrated into municipal garbage collection vehicles.

                  🚛 MUNICIPAL TRUCK
                         │
                         ▼
                ┌────────────────┐
                │  Truck Hopper  │
                └───────┬────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Vibrating / Slanted │
             │       Chute         │
             └──────────┬──────────┘
                        │
                        ▼
                 Waste Alignment
                        │
                        ▼
        ┌──────────────────────────────┐
        │       Detection System       │
        │                              │
        │ 📷 Camera                    │
        │ 💧 Moisture Sensor           │
        │ 🔩 Metal Detection Sensor    │
        └──────────────┬───────────────┘
                       │
                       ▼
                  🧠 Edge AI
                       │
                       ▼
              Waste Classification
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       ♻️ Dry       🌱 Wet       ☣️ Hazardous
       Waste        Waste          Waste
          │            │            │
          ▼            ▼            ▼
      ┌────────┐   ┌────────┐   ┌──────────┐
      │Comp. 1 │   │Comp. 2 │   │ Comp. 3  │
      └────────┘   └────────┘   └──────────┘
🔬 Sensor Fusion

The proposed production system can combine AI vision with physical sensors.

                    📷 CAMERA
                        │
                        ▼
                 Visual Features
                        │
                        ▼
                     🧠 AI
                        ▲
                        │
            ┌───────────┴───────────┐
            │                       │
            ▼                       ▼
    💧 Moisture Sensor       🔩 Metal Sensor
            │                       │
            └───────────┬───────────┘
                        │
                        ▼
                Final Classification
🛠️ Technology Stack
Software
Python
TensorFlow / Keras
MobileNetV2
OpenCV
PIL
Flask
PySerial
HTML
CSS
JavaScript
Hardware
Arduino UNO
Camera / Webcam
Servo Motors
Waste Bins
Connecting Wires
Proposed Production Hardware
Raspberry Pi / Edge AI Device
Industrial Camera
Moisture Sensor
Metal Detection Sensor
Industrial Actuators
Truck-integrated Waste Compartments
📊 Prototype vs Proposed System
Prototype	Proposed System
📷 Webcam	Industrial Camera
🧠 MobileNetV2	Lightweight Edge AI / Detection Model
💻 Computer	Edge AI Device
⚙️ Arduino UNO	Embedded Controller
🔄 Servo Motors	Industrial Actuators
🗑️ Small Bins	Truck-integrated Compartments
👤 Manual Waste Placement	Automated Waste Feeding
3 Waste Classes	Expandable Waste Categories
💡 Innovation

The project combines:

🧠 Artificial Intelligence
        +
📷 Computer Vision
        +
🔌 Sensors
        +
⚙️ Embedded System
        +
🔄 Automated Actuation
        +
🚛 Smart Truck
        ↓
♻️ Smart Waste Segregation
Core Innovation

AI-based waste identification combined with automated physical waste segregation closer to the collection stage.

📈 Market Viability

Growing demand for smart waste management and cleaner cities creates opportunities for technology-enabled waste handling.

The proposed system can be adapted for:

Municipal waste collection
Private waste management
Institutional waste management
Recycling operations
Waste-processing facilities
👥 Customer Viability

Potential customers and users include:

🏛️ Municipalities

🚛 Private Waste Management Companies

🏫 Large Institutions

♻️ Recycling Organizations

🏭 Waste Processing Facilities
💰 Financial Viability

Potential revenue models can include:

Vehicle Deployment
        +
System Installation
        +
Maintenance
        +
Software Services
        +
Data / Analytics Services

The system is intended to reduce manual sorting effort and support more efficient recyclable material recovery.

🔮 Long-Term Viability

The modular design can support expansion into:

More Municipalities
        ↓
Different Truck Capacities
        ↓
Additional Waste Categories
        ↓
Advanced Sensors
        ↓
Edge AI
        ↓
Monitoring & Analytics
🌱 Social & Environmental Impact

The proposed system is intended to support:

👷 Safer waste handling
♻️ Improved recyclable material recovery
🗑️ Better waste segregation
🌍 Cleaner communities
⚙️ Reduced manual sorting effort
🚛 More efficient municipal waste management
🧪 Prototype Testing

The prototype can be tested using representative waste items from the supported categories.

Testing Flow
Waste Item
    ↓
📷 Camera
    ↓
🧠 AI Prediction
    ↓
📊 Confidence Score
    ↓
🔌 Arduino Command
    ↓
🔄 Servo Activation
    ↓
🗑️ Physical Sorting
Example Output
♻ Recyclable bin opened
Predicted: recyclable
Confidence: 94.5%
☣ Hazardous bin opened
Predicted: hazardous
Confidence: 96.04%
💻 Installation
1. Clone Repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <PROJECT_FOLDER>
2. Create Virtual Environment
python -m venv venv
Windows
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Connect Arduino

Connect Arduino UNO using USB.

Check the COM port:

Arduino IDE
     ↓
Tools
     ↓
Port

Current prototype configuration:

COM9
5. Upload Arduino Code

Open the Arduino sketch and upload it to Arduino UNO.

Close:

❌ Serial Monitor
❌ Serial Plotter

before starting Flask.

The same COM port cannot be used by Arduino IDE and Python at the same time.

▶️ Run the Project

Open the terminal:

cd D:\waste_project

Activate the environment:

venv\Scripts\activate

Go to the web application:

cd web_app

Start Flask:

python app.py

Open the browser:

http://127.0.0.1:5000
🔌 Serial Communication

Python communicates with Arduino through the configured COM port.

Commands
recyclable
hazardous
biodegradable
Arduino Mapping
recyclable
     ↓
    D8
     ↓
♻️ Recyclable Servo


hazardous
     ↓
    D9
     ↓
☣️ Hazardous Servo
⚠️ COM Port Troubleshooting

If you see:

PermissionError(13, 'Access is denied.')

the COM port is probably being used by another application.

Close:
❌ Arduino Serial Monitor
❌ Arduino Serial Plotter
❌ Another Flask process
❌ Another Python process
❌ Other applications using COM9

Then restart:

python app.py
📁 Project Structure
AI-Smart-Waste-Segregation/
│
├── web_app/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── ...
│
├── models/
│   └── waste_model_transfer_finetuned2.h5
│
├── arduino/
│   └── waste_sorting.ino
│
├── dataset/
│   ├── recyclable/
│   ├── biodegradable/
│   └── hazardous/
│
├── requirements.txt
│
└── README.md
📌 Project Status
✅ Completed
 AI waste classification
 MobileNetV2 transfer learning
 Camera-based prediction
 Flask web interface
 Arduino communication
 Recyclable servo control
 Hazardous servo control
 Three waste categories
 Prototype hardware integration
🚧 Future Development
 Moisture sensor integration
 Metal sensor integration
 Edge AI deployment
 Automated waste feeding
 Waste alignment mechanism
 Industrial actuator integration
 Municipal truck integration
 Additional waste categories
 Monitoring dashboard
 Waste analytics
 Real-world dataset expansion
🗺️ Development Roadmap
🔄 Future Production Architecture
🎯 Vision
                 CURRENT PROTOTYPE
                        ↓
               🧠 AI Classification
                        ↓
                 ⚙️ Arduino System
                        ↓
                  🔄 Servo Sorting
                        ↓
                🚛 Smart Waste Truck
                        ↓
              ♻️ Intelligent Segregation
                        ↓
                🌍 Cleaner Communities

From AI-based waste recognition to intelligent waste segregation inside municipal collection vehicles.

🏆 Project Highlights
🧠 AI-Based Classification

📷 Computer Vision

⚙️ Embedded Hardware

🔌 Serial Communication

🔄 Automated Servo Control

♻️ Waste Segregation

🚛 Municipal Integration Concept

🌱 Clean & Green Technology
👨‍💻 Contributors
Team Name:

Project Lead:

AI / ML:

Hardware:

Software:

Documentation:

Design:
📜 License

This project is intended for:

Educational purposes
Prototype development
Research
Innovation
Demonstration
