from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import subprocess
import time
import sys

print("🚀 Starting Flask app...")

# Start Flask app
process = subprocess.Popen(
    ["python", "app.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Wait for server
time.sleep(8)

# Headless Chrome (Jenkins compatible)
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

service = Service(ChromeDriverManager().install())

try:
    driver = webdriver.Chrome(service=service, options=options)

    print("🌐 Opening app...")
    driver.get("http://127.0.0.1:5000")

    time.sleep(5)

    if "Healthcare" in driver.page_source:
        print("✅ Selenium Test Passed")
    else:
        print("❌ Content not found")
        sys.exit(1)

    driver.quit()
    process.terminate()

except Exception as e:
    print("❌ Selenium Test Failed:", e)
    process.terminate()
    sys.exit(1)
