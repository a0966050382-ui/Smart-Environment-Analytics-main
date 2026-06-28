from flask import Flask, render_template
from database.database import connect_db, create_table
from crawler.crawler import insert_environment_data
from analysis.analysis import analyze_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

    if conn:
        conn.close()
        return "Flask + PostgreSQL 連線成功！"
    else:
        return "Database connection failed"


@app.route("/create-table")
def create():
    create_table()
    return "Table created!"


@app.route("/insert-data")
def insert_data():
    insert_environment_data()
    return "Data inserted!"


@app.route("/analyze")
def analyze():
    data = analyze_data()

    if data:
        return f"""
        平均溫度: {data['avg_temp']:.2f}°C <br>
        平均濕度: {data['avg_humidity']:.2f}% <br>
        平均 AQI: {data['avg_aqi']:.2f} <br>
        最大 AQI: {data['max_aqi']} <br>
        最小 AQI: {data['min_aqi']}
        """
    
    return "No data found"


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)