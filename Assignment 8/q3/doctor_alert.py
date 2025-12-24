import paho.mqtt.client as mqtt
from datetime import datetime

def on_message(client, userdata, msg):
    time = datetime.now().strftime("%H:%M:%S")
    alert = msg.payload.decode()
    print(f"🚨 {time} | Doctor Alert → {alert}")

# Create MQTT client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)

# Subscribe only to alert topic
client.subscribe("health/alert")
client.on_message = on_message

print("✅ Doctor alert system running...")
client.loop_forever()
