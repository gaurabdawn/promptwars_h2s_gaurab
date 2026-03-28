# Project Setu (सेतु) 🌉
### The Universal AI Bridge for Indian Societal Benefit

[![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![Gemini](https://img.shields.io/badge/Gemini_AI-8E75E5?style=for-the-badge&logo=google-gemini&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)

**Project Setu (सेतु)** is a Gemini-powered "Universal Bridge" designed to close the gap between chaotic, unstructured human intent and rigid, structured emergency/healthcare systems in India. 

In a crisis, data is never clean. Setu ingests "messy" real-world inputs—Hinglish voice notes, blurry prescription photos, or frantic disaster reports—and instantly converts them into **Structured, Verified, and Life-Saving Actions.**

---

## 🏗️ System Design Diagram

```mermaid
graph TD
    subgraph "1. Multimodal Ingestion (The Mess)"
        A[User Intent: Voice/Text/Hinglish] --> D[Setu Gateway]
        B[Evidence: Accident Photos/Prescriptions] --> D
    end

    subgraph "2. Security & Perception (The Shield)"
        D --> E[FastAPI /main.py]
        E --> F[SetuSecurity: PII Redaction]
        F -- "Masked Aadhaar/PAN/Phone" --> G[Gemini 1.5/2.0 Flash]
    end

    subgraph "3. Reasoning Core (The Bridge)"
        G -- "Contextual Reasoning" --> H{Action Logic}
        H -- "Medical" --> I[ABDM Mapping]
        H -- "Disaster" --> J[112/NDRF Logic]
        H -- "Public Safety" --> K[Metro/CISF Logic]
    end

    subgraph "4. Google Cloud Infrastructure (The Scale)"
        H --> L[Cloud Storage: Evidence Persistence]
        H --> M[Firestore: Incident Tracking]
        H --> N[Cloud TTS: Accessibility Voice Output]
    end

    subgraph "5. Structured Output (The Action)"
        N --> O[Structured JSON Action]
        M --> P[Responder Dashboard]
    end
