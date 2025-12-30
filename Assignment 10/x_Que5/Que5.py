from flask import Flask, request
import mysql.connector
from datetime import datetime
import paho.mqtt.publish as publish

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="iot_application"
)
cursor = db.cursor()

THRESHOLD = 30
MQTT_BROKER = "broker.hivemq.com"

@app.route('/moisture', methods=['POST'])
def moisture():
    data = request.json
    sensor_id = data['sensor_id']
    moisture = data['moisture']

    now = datetime.now()
    query = "INSERT INTO moisture_data VALUES (%s,%s,%s)"
    cursor.execute(query, (sensor_id, moisture, now))
    db.commit()

    if moisture < THRESHOLD:
        publish.single("alert/moisture",
                       "Moisture Low!",
                       hostname=MQTT_BROKER)

    return "Stored Successfully"

if __name__ == '__main__':
    app.run(debug=True)
