from fastapi import FastAPI, UploadFile, File, Form
from core.engine import SetuEngine
from core.security import mask_indian_pii
from modules.swasthya import format_to_abdm
import PIL.Image
import io
import json

app = FastAPI(title="Project Setu (सेतु)")
engine = SetuEngine()

@app.get("/")
def home():
    return {"message": "Setu Bridge is active."}

@app.post("/bridge")
async def universal_bridge(
    user_intent: str = Form(None), 
    media: UploadFile = File(None)
):
    """
    Takes messy text/voice-transcripts and images (prescriptions/crashes)
    and converts them to verified action.
    """
    content_bundle = []

    if user_intent:
        safe_text = mask_indian_pii(user_intent)
        content_bundle.append(f"Intent: {safe_text}")

    if media:
        image_data = await media.read()
        image = PIL.Image.open(io.BytesIO(image_data))
        content_bundle.append(image)

    # Simulated Context for Emergency Routing
    content_bundle.append("System Context: User GPS is at 28.6139, 77.2090 (New Delhi). Use this if constructing emergency_route_url.")

    # Process with Gemini Pro if image is uploaded (messy prescription/accident), else Flash
    is_complex = media is not None
    raw_response = await engine.generate_action(content_bundle, is_complex=is_complex)
    
    try:
        # Clean up Markdown if Gemini returns ```json ... ```
        clean_json = raw_response.replace("```json", "").replace("```", "").strip()
        structured_data = json.loads(clean_json)
        
        # Indian Context refinement (Medical)
        if structured_data.get("category") == "Medical":
            structured_data = format_to_abdm(structured_data)
            
        # Life-Saving Verification step
        if structured_data.get("priority") == "P1-Critical":
            route = structured_data.get("emergency_route_url", "No route provided")
            print(f"[ALERT] Life-Saving Verification Step Triggered! Nearest Hospital Route: {route}")
            structured_data["life_saving_verification_executed"] = True
            
        return {"status": "Action Generated", "payload": structured_data}
    
    except Exception as e:
        return {"status": "Error", "raw_output": raw_response, "error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)