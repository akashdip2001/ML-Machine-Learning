import cv2
import mediapipe as mp
import face_recognition
import requests
import numpy as np

# Face recognition setup
known_face_encodings = [face_recognition.face_encodings(face_recognition.load_image_file("authorized.jpg"))[0]]
known_face_names = ["You"]

# Mediapipe setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands()

# ESP32 settings
ESP32_IP = "http://192.168.4.1"  # Change to your ESP32 IP
last_command = None

def detect_hand_state(hand_landmarks):
    # Closed if tip y > pip y (for all fingers), open otherwise
    finger_states = []

    # Thumb (compare tip and IP in x because of orientation)
    finger_states.append(1 if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x else 0)

    # Other fingers
    for tip_id, pip_id in zip([8, 12, 16, 20], [6, 10, 14, 18]):
        finger_states.append(1 if hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[pip_id].y else 0)

    return "open" if sum(finger_states[1:]) > 3 else "closed"

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Face recognition
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    face_authorized = False

    for encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, encoding)
        face_authorized = True if True in matches else face_authorized

    if face_authorized:
        cv2.putText(frame, "AUTHORIZED ✅", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    else:
        cv2.putText(frame, "UNAUTHORIZED ❌", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    # Hand detection
    results = hands.process(rgb_frame)
    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmark, mp_hands.HAND_CONNECTIONS)
            if face_authorized:
                hand_state = detect_hand_state(hand_landmark)
                if hand_state == "closed" and last_command != "on":
                    requests.get(f"{ESP32_IP}/on")
                    last_command = "on"
                elif hand_state == "open" and last_command != "off":
                    requests.get(f"{ESP32_IP}/off")
                    last_command = "off"
            else:
                cv2.putText(frame, "Access Denied", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Fan Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
