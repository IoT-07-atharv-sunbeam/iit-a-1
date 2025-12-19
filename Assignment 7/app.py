from flask import Flask, request, jsonify
from db import execute_query, fetch_all

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route('/')
def home():
    return "Soil Moisture Sensor API is running"

# ---------------- CREATE ----------------
@app.route('/sensor', methods=['POST'])
def add_reading():
    sensor_id = request.form.get('sensor_id')
    moisture = request.form.get('moisture_level')

    query = """
    INSERT INTO soil_moisture (sensor_id, moisture_level)
    VALUES (%s, %s)
    """
    execute_query(query, (sensor_id, moisture))
    return "Sensor reading added successfully"

# ---------------- READ (ALL) ----------------
@app.route('/sensor', methods=['GET'])
def get_all_readings():
    query = "SELECT * FROM soil_moisture"
    data = fetch_all(query)
    return jsonify(data)

# ---------------- UPDATE ----------------
@app.route('/sensor/<int:sensor_id>', methods=['PUT'])
def update_reading(sensor_id):
    moisture = request.form.get('moisture_level')

    query = """
    UPDATE soil_moisture
    SET moisture_level = %s
    WHERE sensor_id = %s
    """
    execute_query(query, (moisture, sensor_id))
    return "Sensor reading updated successfully"

# ---------------- DELETE ----------------
@app.route('/sensor/<int:sensor_id>', methods=['DELETE'])
def delete_reading(sensor_id):
    query = "DELETE FROM soil_moisture WHERE sensor_id = %s"
    execute_query(query, (sensor_id,))
    return "Sensor reading deleted successfully"

# ---------------- THRESHOLD API ----------------
@app.route('/sensor/threshold', methods=['GET'])
def moisture_threshold():
    threshold = request.args.get('value')

    query = """
    SELECT * FROM soil_moisture
    WHERE moisture_level < %s
    """
    data = fetch_all(query, (threshold,))
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
