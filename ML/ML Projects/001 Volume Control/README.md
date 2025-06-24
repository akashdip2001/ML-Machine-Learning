## 📌 PROJECT PURPOSE

> **Control your computer’s system volume using hand gestures captured by a webcam.**

You move your **thumb and index finger**, and based on the **distance between them**, the system volume changes — like an invisible volume knob.

---

<img src="img/Screenshot%20(24).png">

## ✅ Requirements

Install the following libraries:

<img src="img/Screenshot%20(18).png">

```bash
pip install opencv-python mediapipe pycaw comtypes numpy
```

Great — here is the **complete and improved code for `VolumeHandControlAdvance.py`**, along with an explanation of why it's better than the basic `VolumeHandControl.py`.

---

## ✅ Why `VolumeHandControlAdvance.py` is Better ??

| Feature                               | `VolumeHandControl.py`         | `VolumeHandControlAdvance.py`          |
| ------------------------------------- | ------------------------------ | -------------------------------------- |
| ✅ Volume Smoothing                    | ❌ No                           | ✅ Reduces jitter                       |
| ✅ Area Filter (for noise rejection)   | ❌ No                           | ✅ Ignores tiny/large blobs             |
| ✅ Conditional Volume Set (Pinky Down) | ❌ No                           | ✅ Prevents accidental volume changes   |
| ✅ Visual feedback (green dot if set)  | ⚠️ Only when fingers are close | ✅ Only when pinky is down              |
| ✅ Finger check logic                  | ❌ No                           | ✅ Prevents unintended gesture misfires |

> **more reliable, more accurate, better UX.**

<img src="img/Screenshot%20(25).png">
<img src="img/Screenshot%20(26).png">

> in this above images I use `VolumeHandControl.py` so it's detected two hands. </br>
> In the Advance version, the logic is improved.

<img src="img/Screenshot%20(23).png">

---

## 🔗 PROJECT STRUCTURE OVERVIEW

There are **two key files**:

1. **`HandTrackingModule.py`** – a *custom module* that tracks hands using MediaPipe
2. **`VolumeHandControl.py` / `VolumeHandControlAdvance.py`** – the *main script* that uses the hand tracker to adjust volume

---

## 🧱 ARCHITECTURE DIAGRAM (ASCII Format)

```
              +--------------------------+
              |      Your Webcam         |
              +------------+-------------+
                           |
                     Captures Frames
                           ↓
              +------------+-------------+
              |   VolumeHandControl.py   |   ← Main App
              |--------------------------|
              | Uses HandTrackingModule  |
              +------------+-------------+
                           |
                 Calls detect/find functions
                           ↓
              +---------------------------+
              |   HandTrackingModule.py   |  ← Custom Helper Module
              |---------------------------|
              | Uses MediaPipe for        |
              | hand landmark detection   |
              +---------------------------+
                           |
           Returns hand landmarks (x, y positions)
                           ↓
      +--------------------------+---------------------+
      |   Main app calculates distance between fingers |
      |   Converts distance to volume level            |
      |   Updates system volume using Pycaw            |
      +--------------------------+---------------------+

```

---

# ✅ COMPLETE GUIDE TO: `VolumeHandControl.py`
> Let's break down the **basic script `VolumeHandControl.py`** **line by line** and explain it in clear, structured parts — from **importing libraries** to **volume control using hand gestures**. This will help **beginners understand** every single part of the code.

---

### 📁 Part 1: Import Libraries

```python
import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
```

### 🔍 Explanation:

| Line                          | Explanation                                                 |
| ----------------------------- | ----------------------------------------------------------- |
| `cv2`                         | OpenCV: used for accessing the webcam and drawing on screen |
| `time`                        | Used to calculate FPS (frames per second)                   |
| `numpy`                       | Used for math functions like interpolation                  |
| `HandTrackingModule`          | Our custom module to detect and track hands                 |
| `math`                        | Used for calculating distances between finger points        |
| `ctypes`, `comtypes`, `pycaw` | Used to control system volume on Windows                    |

---

### 📁 Part 2: Setup the Camera

```python
wCam, hCam = 640, 480  # width and height of the camera

cap = cv2.VideoCapture(0)  # Start webcam (0 = default camera)
cap.set(3, wCam)  # Set width
cap.set(4, hCam)  # Set height
pTime = 0  # previous time, used for FPS calculation
```

### 🔍 Explanation:

| Line              | What it does                           |
| ----------------- | -------------------------------------- |
| `wCam`, `hCam`    | Target resolution of the webcam window |
| `VideoCapture(0)` | Initializes the webcam                 |
| `.set(3, wCam)`   | Set width (ID `3` in OpenCV)           |
| `.set(4, hCam)`   | Set height (ID `4`)                    |
| `pTime`           | Used to calculate FPS later            |

---

### 📁 Part 3: Initialize Hand Detector

```python
detector = htm.handDetector(detectionCon=0.7)
```

### 🔍 Explanation:

* Creates an object `detector` from the `handDetector` class in `HandTrackingModule`.
* `detectionCon=0.7` means the hand detection confidence must be **70% or more**.

---

### 📁 Part 4: Set Up Volume Control

```python
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
```

### 🔍 Explanation:

| Line               | What it does                                                        |
| ------------------ | ------------------------------------------------------------------- |
| `GetSpeakers()`    | Access the speaker hardware                                         |
| `Activate(...)`    | Get access to the audio control interface                           |
| `cast(...)`        | Converts it to a usable Python object                               |
| `GetVolumeRange()` | Returns min and max values of system volume (e.g., -65.0 to 0.0 dB) |
| `minVol`, `maxVol` | Save these values for use in volume mapping later                   |

---

### 📁 Part 5: Initialize Volume UI Variables

```python
vol = 0          # raw volume in dB
volBar = 400     # y-position of volume bar
volPer = 0       # volume percentage (0–100)
```

---

### 📁 Part 6: Start Main Loop

```python
while True:
    success, img = cap.read()  # Read one frame from the camera
```

### 🔍 Explanation:

* The `while` loop keeps the program running.
* `img` contains the image (frame) from the webcam.
* `success` is `True` if a frame was read successfully.

---

### 📁 Part 7: Find the Hand

```python
img = detector.findHands(img)
lmList = detector.findPosition(img, draw=False)
```

### 🔍 Explanation:

| Function         | What it does                                                            |
| ---------------- | ----------------------------------------------------------------------- |
| `findHands()`    | Detects hands in the frame and draws landmarks                          |
| `findPosition()` | Returns a list of hand landmark positions: `lmList = [[id, x, y], ...]` |

---

### 📁 Part 8: Use Thumb & Index for Volume Control

```python
if len(lmList) != 0:
    x1, y1 = lmList[4][1], lmList[4][2]  # Thumb tip
    x2, y2 = lmList[8][1], lmList[8][2]  # Index tip
    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  # Midpoint
```

### 🔍 Explanation:

* If the hand is detected, we use:

  * `lmList[4]`: Thumb tip
  * `lmList[8]`: Index finger tip
* Then calculate the center point `(cx, cy)` to draw later.

---

### 📁 Part 9: Draw Circles and Line

```python
cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
```

### 🔍 Explanation:

* Draws **visual markers** on your fingers and the connecting line between thumb and index.
* Makes the UI easier to understand.

---

### 📁 Part 10: Calculate Distance Between Fingers

```python
length = math.hypot(x2 - x1, y2 - y1)
```

### 🔍 Explanation:

* `math.hypot(a, b)` calculates the distance between two points using Pythagoras:

  $$
  \text{distance} = \sqrt{(x2 - x1)^2 + (y2 - y1)^2}
  $$

---

### 📁 Part 11: Convert Distance to Volume

```python
vol = np.interp(length, [50, 300], [minVol, maxVol])
volBar = np.interp(length, [50, 300], [400, 150])
volPer = np.interp(length, [50, 300], [0, 100])
volume.SetMasterVolumeLevel(vol, None)
```

### 🔍 Explanation:

* `np.interp()` maps values from one range to another.

  * If fingers are close (`length=50`) → volume low (`minVol`)
  * If fingers are far (`length=300`) → volume high (`maxVol`)
* `volBar`: position of the bar for UI
* `volPer`: percentage for display
* `SetMasterVolumeLevel()`: actually changes the system volume (in decibels)

---

### 📁 Part 12: Visual Feedback

```python
if length < 50:
    cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
```

* If your fingers are very close (volume minimum), draw a green dot at the center.

---

### 📁 Part 13: Draw Volume UI

```python
cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
```

### 🔍 Explanation:

* Volume **bar**: blue rectangle that fills according to volume
* Volume **percentage**: shown as text (e.g., "42 %")

---

### 📁 Part 14: FPS Display

```python
cTime = time.time()
fps = 1 / (cTime - pTime)
pTime = cTime
cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
```

### 🔍 Explanation:

* Shows how fast your camera is processing (frames per second)
* `pTime` is updated every frame to calculate FPS

---

### 📁 Part 15: Show Frame and Wait for Exit

```python
cv2.imshow("Img", img)
cv2.waitKey(1)
```

### 🔍 Explanation:

* Shows the result on a window named `"Img"`
* `waitKey(1)` waits for 1 millisecond before next frame (used in real-time loops)

---

## ✅ RESULT

* Move your **thumb and index** apart → volume increases.
* Bring them close → volume decreases.
* You see the volume % and bar update in real-time.
* Visual markers show where your fingers are.
