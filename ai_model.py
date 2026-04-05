try:
    import whisper
    model = whisper.load_model("base")
    WHISPER_AVAILABLE = True
except:
    print("Whisper not installed → fallback mode")
    WHISPER_AVAILABLE = False

EMERGENCY_KEYWORDS = [
    "chest pain",
    "heart attack",
    "stroke",
    "breathing difficulty",
    "unconscious",
    "severe bleeding",
    "critical condition"
]

def transcribe_audio(file_path):
    if WHISPER_AVAILABLE:
        try:
            result = model.transcribe(file_path)
            return result["text"]
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "patient has chest pain emergency"   # fallback text

def detect_emergency(text):
    text = text.lower()
    alerts = [kw for kw in EMERGENCY_KEYWORDS if kw in text]
    return (len(alerts) > 0), alerts
