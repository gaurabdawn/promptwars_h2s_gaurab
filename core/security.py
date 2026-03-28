import re
import logging

class SetuSecurity:
    @staticmethod
    def sanitize_input(text: str) -> str:
        if not text: return ""
        
        # 1. Mask Aadhaar: Matches 1234-5678-9012, 1234 5678 9012, or 123456789012
        text = re.sub(r'\b\d{4}[ \-]?\d{4}[ \-]?\d{4}\b', '[AADHAAR_REDACTED]', text)
        
        # 2. Mask PAN Card: Standard Indian Format
        text = re.sub(r'\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b', '[PAN_REDACTED]', text)
        
        # 3. Mask Mobile: 10-digit Indian numbers starting with 6-9
        text = re.sub(r'\b[6-9]\d{9}\b', '[PHONE_REDACTED]', text)
        
        return text

    @staticmethod
    def validate_api_key():
        import os
        key = os.getenv("GOOGLE_API_KEY")
        if not key or len(key) < 10:
            logging.error("Security Alert: Invalid or Missing Google API Key")
            return False
        return True