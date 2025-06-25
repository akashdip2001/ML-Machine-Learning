import cv2
import time
import serial
import HandTrackingModule as htm

# Serial connection to Arduino
try:
    arduino = serial.Serial('COM4', 9600)
    time.sleep(2)
    print("✅ Arduino connected on COM4")
except:
    arduino = None
    print("⚠️ Arduino not connected. Serial port failed.")

# Setup camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = htm.handDetector(detectionCon=0.7, maxHands=1)

# States
ledState = False
hoverCounter = 0
hoverThreshold = 20

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]  # Thumb tip
        x2, y2 = lmList[8][1], lmList[8][2]  # Index tip
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        # Virtual ON button
        if 100 < cx < 200 and 50 < cy < 150:
            hoverCounter += 1
            if hoverCounter > hoverThreshold and not ledState:
                if arduino:
                    arduino.write(b'ON\n')
                ledState = True
        # Virtual OFF button
        elif 300 < cx < 400 and 50 < cy < 150:
            hoverCounter += 1
            if hoverCounter > hoverThreshold and ledState:
                if arduino:
                    arduino.write(b'OFF\n')
                ledState = False
        else:
            hoverCounter = 0

    # Draw UI buttons
    onColor = (0, 255, 0) if ledState else (150, 255, 150)
    offColor = (0, 0, 255) if not ledState else (255, 150, 150)

    cv2.rectangle(img, (100, 50), (200, 150), onColor, cv2.FILLED)
    cv2.putText(img, 'ON', (125, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv2.rectangle(img, (300, 50), (400, 150), offColor, cv2.FILLED)
    cv2.putText(img, 'OFF', (320, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    # Show FPS
    cv2.putText(img, time.strftime('%H:%M:%S'), (10, 470), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 2)

    # Display result
    cv2.imshow("LED Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
