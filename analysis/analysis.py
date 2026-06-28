from database.database import connect_db

def analyze_data():
    conn = connect_db()

    if conn:
        cur = conn.cursor()

        cur.execute("""
            SELECT temperature, humidity, aqi
            FROM environment_data
        """)

        rows = cur.fetchall()

        cur.close()
        conn.close()

        if not rows:
            return None

        temperatures = [row[0] for row in rows]
        humidities = [row[1] for row in rows]
        aqis = [row[2] for row in rows]

        result = {
            "avg_temp": sum(temperatures) / len(temperatures),
            "avg_humidity": sum(humidities) / len(humidities),
            "avg_aqi": sum(aqis) / len(aqis),
            "max_aqi": max(aqis),
            "min_aqi": min(aqis)
        }

        return result