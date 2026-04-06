from flask import Flask, render_template, request, jsonify
import os

from ai_model import transcribe_audio, detect_emergency
from db import save_record, get_all_records
from analytics import generate_analytics

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def index():
    try:
        return render_template("index.html")
    except:
        return "Healthcare AI Running"


@app.route("/upload", methods=["POST"])
def upload_audio():
    if "audio" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["audio"]
    patient_name = request.form.get("patient_name")

    if file.filename == "":
        return jsonify({"error": "Empty file name"})

    # Ensure uploads folder exists
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    # Save file properly
    file.save(filepath)

    print("Saved file at:", filepath)

    # Check file exists
    if not os.path.exists(filepath):
        return jsonify({"error": "File not saved properly"})

    # AI Processing
    transcription = transcribe_audio(filepath)
    emergency, alerts = detect_emergency(transcription)

    try:
        save_record(patient_name, transcription, emergency, alerts, file.filename)
    except Exception as e:
        print("DB Error:", e)

    return jsonify({
        "transcription": transcription,
        "emergency": emergency,
        "alerts": alerts
    })


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/analytics")
def analytics():
    data = generate_analytics()
    return jsonify(data)


@app.route("/patients")
def patients():
    records = get_all_records()
    return render_template("patients.html", records=records)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
