import re

def mask_indian_pii(text: str) -> str:
    """Masks Aadhaar numbers (12 digits) and Indian Mobile numbers."""
    # Mask 12-digit Aadhaar
    text = re.sub(r'\b\d{12}\b', '[AADHAAR_MASKED]', text)
    # Mask 10-digit Indian Mobile (starts with 6-9)
    text = re.sub(r'\b[6-9]\d{9}\b', '[PHONE_MASKED]', text)
    return text