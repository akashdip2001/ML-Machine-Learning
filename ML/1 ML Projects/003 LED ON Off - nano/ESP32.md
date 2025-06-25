## CODE (UNO)

```cpp
#ifndef LED_PIN
#define LED_PIN 13  // Onboard LED pin on Arduino Uno
#endif

String input = "";
bool ledState = false;

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);  // Start with LED OFF
}

void loop() {
  if (Serial.available()) {
    input = Serial.readStringUntil('\n');
    input.trim();  // Remove trailing newline or space

    if (input == "ON") {
      ledState = true;
      digitalWrite(LED_PIN, HIGH);  // Turn ON LED
    }
    else if (input == "OFF") {
      ledState = false;
      digitalWrite(LED_PIN, LOW);   // Turn OFF LED
    }
  }
}
```

## for nano

```ini
[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
monitor_speed = 115200
upload_speed = 921600
build_flags =
    -DLED_PIN=5
```

## for UNO

```ini
[env:uno]
platform = atmelavr
board = uno
framework = arduino
monitor_speed = 9600
upload_speed = 115200
build_flags =
    -DLED_PIN=13
```