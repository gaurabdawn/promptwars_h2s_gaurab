import io
import json
import re
import uuid
import PIL.Image
import os
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from dotenv import load_dotenv

# 1. Load Environment Variables
load_dotenv()

# 2. Imports for Cloud Services
try:
    from core.engine import SetuEngine
    from core.security import SetuSecurity
    from core.models import BridgeOutput
    from core.cloud_services import GoogleSetuServices
    from core.accessibility import SetuVoice
    CLOUD_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ Cloud libraries missing: {e}")
    CLOUD_AVAILABLE = False

# 3. INITIALIZE APP (This MUST come before @app decorators)
app = FastAPI(title="Project Setu (सेतु) - Full Cloud Native")

# 4. Initialize Core Logic
engine = SetuEngine()
if CLOUD_AVAILABLE:
    cloud = GoogleSetuServices()
    voice = SetuVoice()

# --- ROUTES ---

@app.get("/")
def root():
    return {
        "message": "Setu Bridge is active.",
        "version": "3.0-cloud-native",
        "google_services": "Enabled" if CLOUD_AVAILABLE else "Disabled"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "Google Cloud Run"}

@app.post("/bridge", response_model=BridgeOutput)
async def universal_bridge(user_intent: str = Form(None), media: UploadFile = File(None)):
    incident_id = str(uuid.uuid4())
    content_bundle = []
    media_url = None

    # A. SECURITY & STORAGE
    if user_intent:
        safe_text = SetuSecurity.sanitize_input(user_intent)
        content_bundle.append(f"Intent: {safe_text}")

    if media and CLOUD_AVAILABLE:
        img_bytes = await media.read()
        # Efficiency: Save messy evidence to Google Cloud Storage
        media_url = cloud.upload_media(incident_id, img_bytes, media.filename)
        # Re-read for AI processing
        image = PIL.Image.open(io.BytesIO(img_bytes))
        content_bundle.append(image)

    try:
        # B. REASONING (The Bridge)
        raw_ai_text = await engine.generate_action(content_bundle)
        clean_json = re.sub(r'^```(?:json)?\n?|(?:\n?| )```$', '', raw_ai_text.strip())
        messy_payload = json.loads(clean_json)

        # C. DATABASE & PERSISTENCE
        if CLOUD_AVAILABLE:
            db_data = {
                "incident_id": incident_id,
                "payload": messy_payload,
                "media_url": media_url,
                "status": "Reported",
                "timestamp": "auto" # Firestore uses server-side timestamp
            }
            cloud.save_incident(incident_id, db_data)

        return BridgeOutput(status="Success", payload=messy_payload)

    except Exception as e:
        return BridgeOutput(status="Error", error=str(e))