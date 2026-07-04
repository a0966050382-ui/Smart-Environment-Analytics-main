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

        temperatures = [float(row[0]) for row in rows]
        humidities = [float(row[1]) for row in rows]
        aqis = [float(row[2]) for row in rows]

        result = {
            "total_records": len(rows),

            "avg_temp": round(sum(temperatures) / len(temperatures), 2),
            "max_temp": max(temperatures),
            "min_temp": min(temperatures),

            "avg_humidity": round(sum(humidities) / len(humidities), 2),

            "avg_aqi": round(sum(aqis) / len(aqis), 2),
            "max_aqi": max(aqis),
            "min_aqi": min(aqis)
        }

        return result