# Setu Architecture: The Bridge Flow

1. **Ingestion (Messy Input):** 
   Accepts unstructured streams: 
   - Audio (AMR/WAV/MP3)
   - Images (JPG/PDF/Handwritten)
   - Real-time News/Weather feeds

2. **Reasoning (The Setu Core):**
   - Uses Gemini Multimodal prompting.
   - Cross-references input against "Knowledge Modules" (swasthya, sahayak, vahan).

3. **Structured Output (Verified Action):**
   - Converts reasoning into a strictly formatted JSON.
   - Triggers the appropriate API endpoint (e.g., Hospital EHR or Emergency Dispatch).