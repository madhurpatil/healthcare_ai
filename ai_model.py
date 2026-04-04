import whisper
from pydub import AudioSegment
import os

model = whisper.load_model("base")

EMERGENCY_KEYWORDS = [
    "chest pain",
    "heart attack",
    "stroke",
    "breathing difficulty",
    "unconscious",
    "severe bleeding",
    "critical condition"
]


def convert_to_wav(input_path):
    output_path = input_path + ".wav"
    
    try:
        audio = AudioSegment.from_file(input_path)
        audio.export(output_path, format="wav")
        return output_path
    except Exception as e:
        print("Conversion error:", e)
        return input_path


def transcribe_audio(file_path):
    try:
        # Convert to wav first
        wav_path = convert_to_wav(file_path)

        result = model.transcribe(wav_path)
        return result["text"]

    except Exception as e:
        return f"Transcription Error: {str(e)}"


def detect_emergency(text):
    text = text.lower()
    alerts = [kw for kw in EMERGENCY_KEYWORDS if kw in text]

    return (len(alerts) > 0), alerts