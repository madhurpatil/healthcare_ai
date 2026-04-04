import os
from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
from datetime import datetime

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client["healthcare_ai"]

patients_col = db["patients"]
records_col = db["records"]


# Save patient (optional)
def save_patient(name):
    patient = {
        "name": name,
        "created_at": datetime.now()
    }
    patients_col.insert_one(patient)


# Save AI record
def save_record(patient_name, transcription, emergency, alerts, filename):
    record = {
        "patient_name": patient_name,
        "transcription": transcription,
        "emergency": emergency,
        "alerts": alerts,
        "audio_file": filename,
        "timestamp": datetime.now()
    }
    records_col.insert_one(record)


def get_all_records():
    return list(records_col.find({}, {"_id": 0}))