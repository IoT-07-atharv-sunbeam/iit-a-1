void setup() {
  Serial.begin(115200);   // UART initialization
}

void loop() {
  Serial.println("Hello from ESP32 via UART");
  delay(2000);
}
