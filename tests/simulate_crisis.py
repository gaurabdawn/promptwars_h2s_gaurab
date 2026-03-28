import httpx
import asyncio
import io
from PIL import Image, ImageDraw, ImageFilter

def create_blurry_prescription():
    # Create a simulated blurry handwritten note
    img = Image.new('RGB', (400, 200), color=(240, 240, 240))
    d = ImageDraw.Draw(img)
    d.text((20, 50), "Chest pain,\nallergic to Aspirin", fill=(50, 50, 50))
    blurry_img = img.filter(ImageFilter.GaussianBlur(1.5))
    
    img_byte_arr = io.BytesIO()
    blurry_img.save(img_byte_arr, format='JPEG')
    return img_byte_arr.getvalue()

async def test_bridge():
    url = "http://localhost:8000/bridge"
    
    # 1. Generate Blurry Prescription Image
    img_bytes = create_blurry_prescription()
    
    files = {
        'media': ('blurry_prescription.jpg', img_bytes, 'image/jpeg')
    }
    
    # 2. Noisy Hindi Transcript
    data = {
        'user_intent': "Bhaiya meri chhati mein bahut tez dard ho raha hai! Aur haan, Aspirin mat dena, allergy hai mujhe! Jaldi dekho."
    }
    
    print("🚀 Firing Crisis Simulation to Setu Bridge...")
    print("-------------------------------------------------")
    print(f"Transcript: {data['user_intent']}")
    print("Attached: blurry_prescription.jpg (Chest pain, allergic to Aspirin)")
    print("-------------------------------------------------\n")
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(url, data=data, files=files)
            print(f"[HTTP {response.status_code}] Setu Response:\n")
            
            import json
            # Print the structured JSON
            print(json.dumps(response.json(), indent=2, ensure_ascii=False))
            
        except Exception as e:
            print(f"❌ Error connecting to server: Is 'uvicorn main:app' running? \nDetails: {e}")

if __name__ == "__main__":
    asyncio.run(test_bridge())
