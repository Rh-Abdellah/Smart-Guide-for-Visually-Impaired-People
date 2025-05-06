from ultralytics import YOLO
import cv2
import pyttsx3
from utils.tts import speak

# Load model
model = YOLO("yolo_model/yolov8n.pt")  # You can use a custom-trained model

# Initialize TTS
engine = pyttsx3.init()

# Initialize camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame)
    labels = results[0].names
    detections = results[0].boxes.cls.tolist()

    spoken = set()
    for cls in detections:
        obj = labels[int(cls)]
        if obj not in spoken:
            speak(f"Warning, {obj} ahead.")
            spoken.add(obj)

    cv2.imshow("Frame", results[0].plot())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
