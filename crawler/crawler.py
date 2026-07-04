from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from database.database import connect_db
import time

def insert_environment_data():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://www.meteoblue.com/en/weather/today/taipei_taiwan_1668341")

    # 等待網頁載入
    time.sleep(5)

    # 抓目前溫度
    temperature = driver.find_element(
        By.CSS_SELECTOR,
        "div.current-temp"
    ).text

    driver.quit()

    # 去掉 °C
    temperature = temperature.replace("°C", "").replace("°", "").strip()
    temperature = float(temperature)

    # 先保留固定值，下一步再抓
    humidity = 75
    aqi = 42

    conn = connect_db()

    if conn:
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO environment_data (temperature, humidity, aqi)
            VALUES (%s, %s, %s)
        """, (temperature, humidity, aqi))

        conn.commit()
        cur.close()
        conn.close()

        print("Weather data inserted successfully!")