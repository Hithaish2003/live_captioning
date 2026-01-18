🧠 Real-Time Scene Description System using OpenCV & YOLOv8

📌 Overview
This project implements a **Real-Time Scene Description System** that analyzes live webcam video and generates **natural language descriptions** of the scene.  
It focuses on understanding **human–object interactions** such as:

- A person holding a bottle  
- A person using a mobile phone  
- A person holding a teddy bear  
- A person holding a remote control  

The system is designed to work reliably in **noisy and low-light environments** by incorporating video preprocessing and stabilization techniques.


🎯 Key Features
- 📸 Live webcam video processing  
- 🧍 Person and object detection using YOLOv8  
- 📝 Scene-level natural language descriptions  
- 🎥 Video recording with captions overlayed  
- 🌙 Noise reduction & contrast enhancement  
- 🖥️ Fullscreen display for demos  
- ⚡ Real-time performance on CPU  

## 🛠️ Tech Stack
- Python  
- OpenCV – video capture, preprocessing, display  
- YOLOv8 (Ultralytics) – real-time object detection  
- NumPy – numerical operations  
- Computer Vision


🧩 System Architecture
Webcam Video
↓
Noise Reduction & Contrast Enhancement
↓
YOLOv8 Object Detection
↓
Scene Understanding Logic
↓
Natural Language Scene Description
↓
Fullscreen Display + Video Recording

▶️ How to Run the Project

1️⃣ Clone the Repository
git clone https://github.com/Hithaish2003/live_captioning.git
cd live_captioning

2️⃣ Install Dependencies
pip install opencv-python ultralytics numpy

3️⃣ Run the Application
python live_captioning.py

Press q to stop recording and exit.
