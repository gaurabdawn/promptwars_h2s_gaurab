import asyncio
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class SetuEngine:
    def __init__(self):
        # Flash is used for efficiency/speed; Pro is for complex medical analysis
        self.flash_model = genai.GenerativeModel('gemini-1.5-flash')
        self.pro_model = genai.GenerativeModel('gemini-1.5-pro')

    async def generate_action(self, prompt_parts: list, is_complex: bool = False):
        system_instruction = """
        You are 'Setu', an emergency bridge for India.
        Convert messy input into a structured ABDM-compliant JSON.
        Provide the output ONLY as a JSON string.
        
        Fields required in the JSON:
        - category: (Medical/Disaster/Traffic)
        - priority: (P1-Critical, P2-Urgent, P3-Stable)
        - summary_hinglish: A 1-sentence summary in Hinglish (Hindi+English).
        - extracted_data: (Blood Group, Allergies, Location, Vehicle No).
        - action_api: The system to trigger (e.g., 'Ambulance_Dispatch').
        - emergency_route_url: If priority is P1-Critical, generate a Google Maps link to the nearest hospital based on the provided or a dynamically simulated GPS coordinate.
        - verification_required: true (if action_api involves physical dispatch like Ambulance/Fire).
        
        DO NOT include any 12-digit Aadhaar or 10-digit phone numbers in the output.
        """
        
        selected_model = self.pro_model if is_complex else self.flash_model
        
        # Implement Exponential Backoff (3 retries)
        max_retries = 3
        base_delay = 1
        for attempt in range(max_retries):
            try:
                response = await selected_model.generate_content_async([system_instruction] + prompt_parts)
                return response.text
            except Exception as e:
                if attempt == max_retries - 1:
                    raise e
                await asyncio.sleep(base_delay * (2 ** attempt))