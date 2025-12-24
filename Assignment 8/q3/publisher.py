import paho.mqtt.client as mqtt
import time

# Create MQTT client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)

print("✅ Patient device started...")

while True:
    # --- Simulated sensor values ---
    pulse = 55     # abnormal pulse (for testing)
    spo2 = 92      # abnormal SpO2 (for testing)

    # Publish values
    client.publish("health/pulse", pulse)
    client.publish("health/spo2", spo2)

    print(f"Sent → Pulse: {pulse}, SpO2: {spo2}")

    time.sleep(5)
