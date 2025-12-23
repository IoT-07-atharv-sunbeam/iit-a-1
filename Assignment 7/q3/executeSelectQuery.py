import mysql.connector

def executeSelectQuery(query):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root@123",
        database="smart_home"
    )
    cur = conn.cursor(dictionary=True)
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data
