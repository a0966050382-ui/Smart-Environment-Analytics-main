import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
            host="dpg-d90mo0flk1mc73cstscg-a.singapore-postgres.render.com",
            database="environment_data",
            user="admin",
            password="rHoBghFgL4N45Dw8ljODNVb2alAnLjlN",
            port="5432"
        )
        print("Database connected successfully!")
        return conn
    except Exception as e:
        print("Connection failed:", e)
        return None
def create_table():
    conn = connect_db()
    
    if conn:
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS environment_data (
                id SERIAL PRIMARY KEY,
                temperature FLOAT,
                humidity FLOAT,
                aqi INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        conn.commit()
        cur.close()
        conn.close()
        print("Table created successfully!")