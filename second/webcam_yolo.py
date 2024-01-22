from ultralytics import YOLO
import cv2

model = YOLO('yolov8l.pt')

# webcam and video
# cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture("motorbikes.mp4")

while True:
    success, img = cap.read()
    # cv2.imshow('webcam', img)
    result = model(img, show=True)
    cv2.waitKey(1)





