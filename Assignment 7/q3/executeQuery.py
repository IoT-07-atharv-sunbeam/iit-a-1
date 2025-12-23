import mysql.connector

def executeQuery(query):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root@123",
        database="smart_home"
    )
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
