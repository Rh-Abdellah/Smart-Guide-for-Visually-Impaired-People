# Smart Guide for Visually Impaired People

This project is a smart assistive system designed to help visually impaired individuals navigate their environment safely. It uses computer vision with the YOLOv8 object detection model on a Raspberry Pi 4 to identify nearby objects and deliver real-time audio feedback for navigation.

## 🧠 Overview

- **Hardware**: Raspberry Pi 4 with a camera module and speaker/headphones.
- **Object Detection**: YOLOv8 (Ultralytics) detects obstacles and objects.
- **Real-Time Feedback**: Audio instructions guide the user based on detected objects and their positions.
- **Programming Language**: Python

## 🛠️ Technologies Used

- **Python 3**
- **OpenCV**
- **YOLOv8 (Ultralytics)**
- **Text-to-Speech (pyttsx3 or gTTS)**
- **Raspberry Pi Camera Module**
- **Raspberry Pi OS**


## 🚀 Getting Started

### Raspberry Pi Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Connect the Pi camera and test with:
    ```bash
    libcamera-hello
    ```

3. Run the detection script:
    ```bash
    python3 main.py
    ```

> Ensure the YOLOv8 model (`yolov8n.pt`) is downloaded and placed in the `yolo_model/` folder.

## 🔊 Features

- Real-time object detection using YOLOv8
- Verbal instructions using TTS
- Lightweight for edge deployment on Raspberry Pi

## 🔧 Requirements

- Raspberry Pi 4
- Camera module
- Speakers or headphones
- Python 3.8+
- Internet (for downloading models if needed)

## 👤 Author

Developed by [Your Name]  
Student in Embedded Systems and Electronics – ENSA Marrakech

## 📜 License

This project is licensed under the MIT License.


