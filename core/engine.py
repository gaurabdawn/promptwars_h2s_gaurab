import google.generativeai as genai
import os
import logging
from dotenv import load_dotenv

load_dotenv()

class SetuEngine:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SetuEngine, cls).__new__(cls)
            genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
            # Efficiency: Pre-load the Flash model
            cls._instance.model = genai.GenerativeModel('models/gemini-flash-latest')
            logging.info("Google Service: Gemini Engine Initialized in Flexible Mode.")
        return cls._instance

    async def generate_action(self, prompt_parts: list) -> str:
        system_instruction = """
        You are 'Setu'. Analyze the input and return the result in JSON format.
        You can return a single object or a list of objects if there are multiple issues.
        REDACT Aadhaar/Phone numbers.
        """
        try:
            response = await self.model.generate_content_async(
                [system_instruction] + prompt_parts,
                generation_config={"response_mime_type": "application/json"}
            )
            return response.text
        except Exception as e:
            logging.error(f"Google AI Service Error: {str(e)}")
            raise e