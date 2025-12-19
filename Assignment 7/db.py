import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root@123",
        database="iotdb"
    )

def execute_query(query, params=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()

def fetch_all(query, params=None):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute(query, params)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data
