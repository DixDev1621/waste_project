AI-Powered Smart Waste Segregation System

An AI-based smart waste segregation system that uses computer vision,
deep learning, Flask, Arduino, and servo-controlled hardware to identify
and physically separate waste.

Overview

The project addresses mixed household waste collection by combining
AI-based classification with automatic physical sorting.

Prototype:
Camera → AI Classification → Flask → Arduino UNO → Servo Motor → Waste
Bin

Proposed municipal system:
Camera + Sensors → Edge AI → Classification → Actuators →
Dry/Wet/Hazardous Compartments

Problem Statement

Mixed waste is difficult and time-consuming to sort manually. Manual
handling can also expose workers to unwanted contact with hazardous
materials.

The project aims to support automated waste identification, safer
handling, improved segregation, and more efficient waste management.

Waste Categories

♻️ Recyclable

🌱 Biodegradable

☣️ Hazardous

Key Features

AI-based waste classification

MobileNetV2 with transfer learning for the prototype

Real-time camera-based prediction

Flask web interface

Arduino UNO control

Serial communication using Python/PySerial

Servo-based physical sorting

Expandable architecture for moisture and metal sensors

Proposed integration with municipal garbage collection vehicles

System Architecture

Camera
   ↓
MobileNetV2 AI Model
   ↓
Flask Web Application
   ↓
Serial Communication
   ↓
Arduino UNO
   ↓
 ┌───────────────┬────────────────┐
 ↓               ↓                ↓
D8 Servo       D9 Servo       No Servo
 ↓               ↓                ↓
Recyclable     Hazardous      Biodegradable

Prototype Workflow

Waste is placed in front of the camera.

The camera captures the image.

The AI model predicts the waste category.

Flask displays the prediction and confidence.

Python sends the category command to Arduino.

Arduino activates the corresponding servo.

The sorting mechanism directs the waste into the appropriate bin.

Technology Stack

Component          Technology

Language           Python
AI Model           MobileNetV2 + Transfer Learning
Image Processing   OpenCV / PIL
Web Framework      Flask
Hardware           Arduino UNO
Communication      PySerial / Serial
Frontend           HTML, CSS, JavaScript
Model Format       H5

AI Model

The current prototype uses MobileNetV2 with transfer learning.

Classes:

biodegradable
hazardous
recyclable

The model receives an image, processes it, and returns the predicted
category with a confidence value.

Hardware Mapping

Recyclable   → Arduino D8 → Servo 1
Hazardous    → Arduino D9 → Servo 2
Biodegradable → No servo in current prototype

Proposed Municipal Garbage-Truck System

The prototype is designed as a foundation for a larger system that can
be integrated into municipal garbage collection vehicles.

Mixed Waste
    ↓
Truck Hopper
    ↓
Vibrating / Slanted Chute
    ↓
Waste Alignment
    ↓
Camera + Moisture + Metal Sensors
    ↓
Edge AI
    ↓
Waste Classification
    ↓
Automatic Actuation
    ↓
┌──────────┬──────────┬───────────┐
│ Dry /    │ Wet /    │ Hazardous │
│ Recycl.  │ Organic  │           │
└──────────┴──────────┴───────────┘

The production concept can combine camera-based recognition with
moisture and metal sensing for additional physical verification.

Prototype vs Proposed System

Prototype      Proposed System

Webcam         Industrial camera
MobileNetV2    Lightweight edge AI / detection model
Computer       Edge AI device
Arduino UNO    Embedded actuator controller
Servo motors   Industrial actuators
Small bins     Truck-integrated compartments
Manual input   Automated waste feeding
3 classes      Expandable waste categories

Innovation

The project combines:

AI-based waste recognition

Physical waste segregation

Sensor-assisted verification

Automated actuator control

In-vehicle waste segregation

The proposed approach moves waste segregation closer to the collection
stage.

Business & Viability

Market Viability

Growing demand for smart waste management and cleaner cities creates
opportunities for automated waste-handling solutions.

Customer Viability

Potential users include:

Municipalities

Private waste management companies

Large institutions

Recycling and waste-processing organizations

Financial Viability

The system can reduce manual sorting effort and support recyclable
material recovery. Potential revenue models can include vehicle
deployment, installation, maintenance, and software/data services.

Long-Term Viability

The modular design can be expanded to different municipalities, truck
capacities, and additional waste categories.

Future Scope

Lightweight YOLO-based detection for production deployment

Raspberry Pi / Jetson-class edge deployment

Moisture and metal sensor fusion

Automatic waste feeding and alignment

Industrial actuators

More waste categories

Truck monitoring dashboard

Waste collection and segregation analytics

Continuous model improvement using real-world waste images

Setup

Clone the repository

git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <PROJECT_FOLDER>

Create virtual environment

python -m venv venv

Windows:

venv\Scriptsctivate

Install dependencies

pip install -r requirements.txt

Start the Flask application

cd web_app
python app.py

Open:

http://127.0.0.1:5000

Arduino

Connect the Arduino UNO through USB and upload the Arduino sketch.

Current prototype mapping:

Recyclable → D8
Hazardous  → D9

Close Arduino Serial Monitor before starting Flask because the same COM
port cannot be used by both programs simultaneously.

Project Status

Completed Prototype

AI waste classification

Camera-based prediction

Flask web interface

Arduino communication

Recyclable servo control

Hazardous servo control

Three waste classes

Planned

Moisture sensor integration

Metal sensor integration

Edge AI deployment

Automated waste feeding

Industrial actuator integration

Municipal truck integration

Expanded waste categories

Monitoring and analytics

Social & Environmental Impact

The proposed system is intended to support:

Safer waste handling

Reduced direct manual contact with mixed waste

Improved waste segregation

Better recyclable material recovery

More efficient municipal waste management

Cleaner communities

Contributors

Add your team members here.

Team Name:
Project Lead:
AI/ML:
Hardware:
Software:
Documentation:

License

This project is intended for educational, prototype, research, and
innovation purposes.
