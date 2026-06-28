from database.database import connect_db

def insert_environment_data():
    conn = connect_db()

    if conn:
        cur = conn.cursor()

        temperature = 29.5
        humidity = 78
        aqi = 42

        cur.execute("""
            INSERT INTO environment_data (temperature, humidity, aqi)
            VALUES (%s, %s, %s)
        """, (temperature, humidity, aqi))

        conn.commit()
        cur.close()
        conn.close()

        print("Data inserted successfully!")