from flask import Flask, render_template
from database.database import connect_db, create_table
from crawler.crawler import insert_environment_data
from analysis.analysis import analyze_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

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
        <h1>📊 Environment Data Analysis</h1>

        <hr>

        <h3>📁 資料筆數：{data['total_records']}</h3>

        <h3>🌡️ Temperature</h3>
        平均溫度：{data['avg_temp']} °C<br>
        最高溫度：{data['max_temp']} °C<br>
        最低溫度：{data['min_temp']} °C<br><br>

        <h3>💧 Humidity</h3>
        平均濕度：{data['avg_humidity']} %<br><br>

        <h3>🌫️ AQI</h3>
        平均 AQI：{data['avg_aqi']}<br>
        最大 AQI：{data['max_aqi']}<br>
        最小 AQI：{data['min_aqi']}<br>
        """

    return "<h2>No data found.</h2>"

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)