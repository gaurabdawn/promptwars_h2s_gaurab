from fastapi import FastAPI, UploadFile, File, Form
from core.engine import SetuEngine
from core.security import SetuSecurity
from core.models import BridgeOutput
import PIL.Image
import io
import json
import re
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Project Setu (सेतु) - Ultimate Flexibility")
engine = SetuEngine()

@app.post("/bridge", response_model=BridgeOutput)
async def universal_bridge(user_intent: str = Form(None), media: UploadFile = File(None)):
    content_bundle = []
    
    # 1. SECURITY: Always sanitize first
    if user_intent:
        safe_text = SetuSecurity.sanitize_input(user_intent)
        content_bundle.append(f"Intent: {safe_text}")

    if media:
        image_data = await media.read()
        image = PIL.Image.open(io.BytesIO(image_data))
        content_bundle.append(image)

    try:
        # 2. Get AI Response
        raw_ai_text = await engine.generate_action(content_bundle)
        
        # 3. Clean Markdown (Security/Quality)
        clean_json = re.sub(r'^```(?:json)?\n?|(?:\n?| )```$', '', raw_ai_text.strip())
        
        # 4. Parse JSON (Could be a list or a dict)
        messy_data = json.loads(clean_json)
        
        # 5. SUCCESS: Pydantic will now accept messy_data regardless of its shape
        return BridgeOutput(status="Success", payload=messy_data)

    except Exception as e:
        # 6. FAIL-SAFE: If Gemini returns something that isn't even JSON
        return BridgeOutput(status="Error", error=str(e))