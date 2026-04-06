from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import subprocess
import requests

print("Starting Flask app...")

# Start Flask app
flask_process = subprocess.Popen(["python", "app.py"])

# Wait until server is ready
for _ in range(10):
    try:
        res = requests.get("http://127.0.0.1:5000")
        if res.status_code == 200:
            break
    except:
        time.sleep(2)

# Headless Chrome
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

service = Service(ChromeDriverManager().install())

try:
    driver = webdriver.Chrome(service=service, options=options)

    print("Opening app...")
    driver.get("http://127.0.0.1:5000")

    time.sleep(5)

    if "Healthcare" in driver.page_source:
        print("Selenium Test Passed")
    else:
        print("Test Failed")
        exit(1)

    driver.quit()

finally:
    flask_process.terminate()
    print("Flask stopped")
