import paho.mqtt.client as mqtt
import mysql.connector

# DB connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123",
    database="healthcare_iot"
)
cursor = db.cursor()

def on_message(client, userdata, msg):
    data = msg.payload.decode()

    # Pulse handling
    if msg.topic == "health/pulse":
        pulse = int(data)
        print("Pulse:", pulse)

        if pulse < 60 or pulse > 100:
            alert = f"Pulse abnormal ({pulse})"
            print("🚨", alert)

            # Send alert
            client.publish("health/alert", alert)

            # AUTO INSERT INTO DB
            cursor.execute(
                "INSERT INTO health_alerts (parameter, value, message) VALUES (%s,%s,%s)",
                ("Pulse", pulse, alert)
            )
            db.commit()

    # SpO2 handling
    elif msg.topic == "health/spo2":
        spo2 = int(data)
        print("SpO2:", spo2)

        if spo2 < 94:
            alert = f"SpO2 low ({spo2})"
            print("🚨", alert)

            client.publish("health/alert", alert)

            # AUTO INSERT INTO DB
            cursor.execute(
                "INSERT INTO health_alerts (parameter, value, message) VALUES (%s,%s,%s)",
                ("SpO2", spo2, alert)
            )
            db.commit()

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)
client.subscribe("health/#")
client.on_message = on_message

print("✅ Subscriber running & waiting for data...")
client.loop_forever()
