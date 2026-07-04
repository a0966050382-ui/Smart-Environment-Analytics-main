from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.meteoblue.com/en/weather/today/taipei_taiwan_1668341")

# 等網頁載入
time.sleep(5)

temperature = driver.find_element(
    By.CSS_SELECTOR,
    "div.cell.no-mobile"
).text

print("Temperature:", temperature)

input("按 Enter 關閉")

driver.quit()