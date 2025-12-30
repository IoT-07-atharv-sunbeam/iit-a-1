#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT11

const char* ssid = "SUNBEAM";
const char* password = "1234567890";
const char* mqttServer = "broker.hivemq.com";

WiFiClient espClient;
PubSubClient client(espClient);
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) delay(500);

  client.setServer(mqttServer, 1883);
}

void loop() {
  if (!client.connected()) {
    while (!client.connected()) {
      client.connect("ESP32_Publisher");
    }
  }

  float t = dht.readTemperature();
  float h = dht.readHumidity();

  if (!isnan(t) && !isnan(h)) {
    client.publish("sensor/temperature", String(t).c_str());
    client.publish("sensor/humidity", String(h).c_str());
  }
  delay(5000);
}
