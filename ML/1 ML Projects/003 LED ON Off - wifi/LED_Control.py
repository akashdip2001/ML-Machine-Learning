import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
import requests

# Webcam size
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# Hand detector
pTime = 0
detector = htm.handDetector(detectionCon=0.7, maxHands=1)

# ESP32 URL
led_url = "http://192.168.1.100"  # Replace with your ESP32 static IP

# UI values
volBar = 400
volPer = 0
sendVal = 0
ledState = "ON"

# Send value to ESP32
def sendToESP32(value):
    try:
        requests.get(f"{led_url}/set?value={value}", timeout=0.2)
    except:
        print("⚠️ Failed to send to ESP32")

# Create OpenCV window and mouse callback ONCE
cv2.namedWindow("Img")

def mouseClick(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if 500 < x < 600:
            if 150 < y < 200:
                sendToESP32(255)  # Turn LED ON
            elif 220 < y < 270:
                sendToESP32(0)    # Turn LED OFF

cv2.setMouseCallback("Img", mouseClick)

# Main loop
while True:
    success, img = cap.read()
    if not success:
        print("❌ Camera not accessible")
        break

    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=True)

    # Hand detected
    if len(lmList) != 0:
        area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100
        if 250 < area < 1000:
            length, img, lineInfo = detector.findDistance(4, 8, img)
            volBar = np.interp(length, [50, 200], [400, 150])
            volPer = np.interp(length, [50, 200], [0, 100])
            smoothness = 5
            volPer = smoothness * round(volPer / smoothness)
            sendVal = int(np.interp(volPer, [0, 100], [0, 255]))

            # If pinky is down, send brightness
            fingers = detector.fingersUp()
            if not fingers[4]:
                sendToESP32(sendVal)
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)

    # Draw brightness bar
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (40, 450),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    # LED ON/OFF Buttons
    cv2.rectangle(img, (500, 150), (600, 200), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, 'LED ON', (510, 185), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.rectangle(img, (500, 220), (600, 270), (0, 0, 255), cv2.FILLED)
    cv2.putText(img, 'LED OFF', (505, 255), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime + 1e-5)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    # Display window
    cv2.imshow("Img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
