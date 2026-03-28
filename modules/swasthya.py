# Medical Module for Ayushman Bharat (ABDM) context
def format_to_abdm(extracted_json):
    """
    Standardizes Gemini output to Indian Health Stack formats.
    """
    return {
        "resourceType": "EmergencyBundle",
        "timestamp": "now",
        "data": extracted_json
    }