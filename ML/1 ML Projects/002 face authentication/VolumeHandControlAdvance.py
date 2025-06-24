import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
import face_recognition
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# ========== SETTINGS ==========
AUTHORIZED_TIME = 5  # seconds of temporary guest access
owner_image_path = "owner.jpg"  # known face image
wCam, hCam = 640, 480
# ==============================

# Load known face
owner_image = face_recognition.load_image_file(owner_image_path)
owner_encoding = face_recognition.face_encodings(owner_image)[0]

# Initialize
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(detectionCon=0.7, maxHands=1)

# Audio
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol, maxVol = volRange[0], volRange[1]

# Variables
vol, volBar, volPer = 0, 400, 0
colorVol = (255, 0, 0)
pTime = 0
authOwner = False
tempAuth = False
tempStart = 0

while True:
    success, img = cap.read()
    if not success:
        break

    small_img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    rgb_small_img = small_img[:, :, ::-1]

    faces = face_recognition.face_locations(rgb_small_img)
    encodings = face_recognition.face_encodings(rgb_small_img, faces)

    authOwner = False

    for encoding in encodings:
        match = face_recognition.compare_faces([owner_encoding], encoding)
        if match[0]:
            authOwner = True
            break

    # Start temp auth if owner in background and guest detected
    if not authOwner and len(encodings) > 0:
        if tempAuth is False:
            tempAuth = True
            tempStart = time.time()

    # Check timer expiration
    if tempAuth and (time.time() - tempStart > AUTHORIZED_TIME):
        tempAuth = False

    # Determine final auth
    canControl = authOwner or tempAuth

    # ========== Hand Detection ==========
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=True)

    if canControl:
        # Show access granted
        cv2.putText(img, "Access: AUTHORIZED", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        if tempAuth and not authOwner:
            remaining = AUTHORIZED_TIME - int(time.time() - tempStart)
            cv2.putText(img, f'Temp Access: {remaining}s', (10, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

        if len(lmList) != 0:
            area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100
            if 250 < area < 1000:
                length, img, lineInfo = detector.findDistance(4, 8, img)
                volBar = np.interp(length, [50, 200], [400, 150])
                volPer = np.interp(length, [50, 200], [0, 100])
                smoothness = 10
                volPer = smoothness * round(volPer / smoothness)
                fingers = detector.fingersUp()

                if not fingers[4]:
                    volume.SetMasterVolumeLevelScalar(volPer / 100, None)
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    colorVol = (0, 255, 0)
                else:
                    colorVol = (255, 0, 0)
    else:
        # Show warning
        cv2.putText(img, "Access: NOT AUTHORIZED", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    # Volume UI
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (40, 450),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    # FPS Display
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (500, 50),
                cv2.FONT_HERSHEY_COMPLEX, 1, (100, 255, 0), 3)

    cv2.imshow("Img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
