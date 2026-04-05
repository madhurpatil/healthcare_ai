from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import subprocess
import time

print("🚀 Starting Flask app...")

# Start Flask app
process = subprocess.Popen(
    ["python", "app.py"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

time.sleep(5)

# 🔥 Headless setup (IMPORTANT)
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")

# 🔥 Force binary location (VERY IMPORTANT)
options.binary_location = "C:\\Users\\Madhur pramod patil\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

try:
    print("🌐 Opening app...")
    driver.get("http://127.0.0.1:5000")

    time.sleep(5)

    if "Healthcare" in driver.page_source:
        print("✅ Selenium Test Passed")
    else:
        print("❌ Page content not found")

except Exception as e:
    print("❌ Selenium Test Failed:", e)
    exit(1)   # 🔥 VERY IMPORTANT FOR JENKINS

finally:
    driver.quit()
    process.terminate()