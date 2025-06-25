## ESP 32 code 

```cpp
#include <WiFi.h>

// WiFi credentials
const char* ssid = "spaceTime";
const char* password = "12345678@12";

// Static IP details
IPAddress local_IP(192, 168, 1, 100);
IPAddress gateway(192, 168, 1, 1);
IPAddress subnet(255, 255, 255, 0);

// Web server on port 80
WiFiServer server(80);

#ifndef LED_PIN
#define LED_PIN 5
#endif

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  analogWrite(LED_PIN, 0);  // Start with LED off

  // Set static IP before WiFi.begin()
  if (!WiFi.config(local_IP, gateway, subnet)) {
    Serial.println("❌ Failed to configure static IP");
  }

  WiFi.begin(ssid, password);
  Serial.print("🔌 Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\n✅ WiFi Connected");
  Serial.print("📶 IP Address: ");
  Serial.println(WiFi.localIP());

  server.begin();
}

void loop() {
  WiFiClient client = server.available();

  if (client) {
    Serial.println("🌐 Client connected");
    String request = client.readStringUntil('\r');
    client.flush();

    // Parse brightness value from URL
    if (request.indexOf("/set?value=") != -1) {
      int valIndex = request.indexOf("value=");
      String valStr = request.substring(valIndex + 6, request.indexOf(" ", valIndex));
      int brightness = valStr.toInt();
      brightness = constrain(brightness, 0, 255);
      analogWrite(LED_PIN, brightness);

      Serial.print("💡 Brightness set to: ");
      Serial.println(brightness);
    }

    // Send HTTP response
    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/html");
    client.println();
    client.println("OK");
    client.stop();
  }
}
```

## platformio.ini

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