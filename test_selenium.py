import subprocess
import time
import requests
import sys

print("🚀 Starting Flask app...")

# Start Flask app
process = subprocess.Popen(
    ["python", "app.py"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

# Wait for server
time.sleep(5)

url = "http://127.0.0.1:5000"

try:
    print("🌐 Sending request to app...")
    response = requests.get(url)

    if response.status_code == 200 and "Healthcare" in response.text:
        print("✅ Test Passed (App is running)")
    else:
        print("❌ Test Failed")
        sys.exit(1)

except Exception as e:
    print("❌ Error:", e)
    sys.exit(1)

finally:
    process.terminate()
