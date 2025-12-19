import sqlite3
from datetime import datetime

conn = sqlite3.connect("sensors.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sensor_readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperature REAL,
    humidity REAL,
    timestamp TEXT
)
""")

def insert_reading(temp, hum):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO sensor_readings (temperature, humidity, timestamp) VALUES (?, ?, ?)",
                   (temp, hum, ts))
    conn.commit()

def get_all_readings():
    cursor.execute("SELECT * FROM sensor_readings")
    return cursor.fetchall()

def update_reading(record_id, new_temp, new_hum):
    cursor.execute("UPDATE sensor_readings SET temperature=?, humidity=? WHERE id=?",
                   (new_temp, new_hum, record_id))
    conn.commit()

def delete_reading(record_id):
    cursor.execute("DELETE FROM sensor_readings WHERE id=?", (record_id,))
    conn.commit()

def get_below_threshold(temp_threshold=None, hum_threshold=None):
    query = "SELECT * FROM sensor_readings WHERE 1=1"
    params = []
    if temp_threshold is not None:
        query += " AND temperature < ?"
        params.append(temp_threshold)
    if hum_threshold is not None:
        query += " AND humidity < ?"
        params.append(hum_threshold)
    
    cursor.execute(query, tuple(params))
    return cursor.fetchall()


insert_reading(25.5, 60.2)
insert_reading(18.3, 40.1)
insert_reading(30.0, 70.0)

print("All Readings:")
for row in get_all_readings():
    print(row)

print("\nReadings below thresholds (temp < 20, hum < 50):")
for row in get_below_threshold(temp_threshold=20, hum_threshold=50):
    print(row)

update_reading(1, 26.0, 61.0)

delete_reading(2)

print("\nFinal Readings after update & delete:")
for row in get_all_readings():
    print(row)

conn.close()