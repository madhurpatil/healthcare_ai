from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import subprocess
import time
import sys
import requests

print("🚀 Starting Flask app...")

# Start Flask app
process = subprocess.Popen(
    ["python", "app.py"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

# 🔥 Wait until server is actually ready (NOT just sleep)
url = "http://127.0.0.1:5000"
for i in range(15):
    try:
        requests.get(url)
        print("✅ Server is ready")
        break
    except:
        time.sleep(1)
else:
    print("❌ Server not starting")
    process.terminate()
    sys.exit(1)

# Headless Chrome (Jenkins safe)
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

service = Service(ChromeDriverManager().install())

try:
    driver = webdriver.Chrome(service=service, options=options)

    print("🌐 Opening app...")
    driver.get(url)

    time.sleep(3)

    if "Healthcare" in driver.page_source:
        print("✅ Selenium Test Passed")
    else:
        print("❌ Content not found")
        sys.exit(1)

    driver.quit()
    process.terminate()

except Exception as e:
    print("❌ Selenium Failed:", e)
    process.terminate()
    sys.exit(1)
