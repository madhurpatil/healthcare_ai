from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import subprocess
import requests

print("Starting Flask app...")

# Start Flask
flask_process = subprocess.Popen(["python", "app.py"])

# Wait until server is actually UP
def wait_for_server(url, timeout=30):
    for _ in range(timeout):
        try:
            requests.get(url)
            return True
        except:
            time.sleep(1)
    return False

if not wait_for_server("http://127.0.0.1:5000"):
    print("Flask failed to start")
    flask_process.terminate()
    exit(1)

print("Flask started successfully")

# Chrome setup
options = Options()
options.binary_location = r"C:\Users\Madhur pramod patil\AppData\Local\Google\Chrome\Application\chrome.exe"

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
        driver.quit()
        flask_process.terminate()
        exit(1)

    driver.quit()

finally:
    flask_process.terminate()
    print("Flask stopped")
