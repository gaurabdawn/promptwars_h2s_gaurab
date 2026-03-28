# Project Setu (सेतु) 🌉

### The Universal AI Bridge for Indian Societal Benefit

[![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![Cloud Run](https://img.shields.io/badge/Cloud_Run-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/run)
[![Firestore](https://img.shields.io/badge/Firestore-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)](https://firebase.google.com/)
[![Gemini](https://img.shields.io/badge/Gemini_AI-8E75E5?style=for-the-badge&logo=google-gemini&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Speech-to-Text](https://img.shields.io/badge/Speech--to--Text-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/speech-to-text)
[![Text-to-Speech](https://img.shields.io/badge/Text--to--Speech-FF6F00?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/text-to-speech)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Cloud Build](https://img.shields.io/badge/Cloud_Build-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/build)

**Project Setu (सेतु)** is a Gemini-powered "Universal Bridge" designed to close the gap between chaotic, unstructured human intent and rigid, structured emergency/healthcare systems in India.

In a crisis, data is never clean. Setu ingests "messy" real-world inputs — Hinglish voice notes, blurry prescription photos, or frantic disaster reports — and instantly converts them into **Structured, Verified, and Life-Saving Actions.**

---

## 🏗️ System Design Diagram

<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/45acac8a-f744-42b8-92e3-0c529d7a5409" />

### 📜 Technical Writeup
## I. Project Philosophy
Project Setu is engineered as a Universal Bridge to solve the "Impedance Mismatch" between human chaos and system structure. In the Indian societal context, emergency data is rarely clean — it is multimodal, vernacular, and high-entropy.
Setu uses a Reasoning-over-Parsing approach to transform this chaos into machine-interoperable, actionable outputs.
## II. Agentic Engineering with Antigravity & Google AI Studio
The intelligence of Setu was developed using a dual-loop AI feedback system:

Google AI Studio: Used for rapid prototyping of system instructions and multimodal testing (blurry Indian medical prescriptions, noisy Hindi audio transcripts, etc.).
Antigravity IDE: The application code was refined using agentic capabilities. A .antigravity/ configuration directory containing rules.md and architecture.md guided the agents to enforce:
Singleton Pattern for Gemini initialization
Zero-Strictness Pydantic models for robust high-stakes data ingestion


## III. Core Architectural Pillars

Multimodal Reasoning Engine: Powered by Gemini 1.5 / 2.0 Flash via the v1beta API. Chosen for high tokens-per-second and low latency — critical for life-saving triage.
PII Sanitization (The Shield): Pre-processing layer in core/security.py redacts sensitive Indian identifiers (Aadhaar, PAN, Mobile) using optimized regex patterns before the payload leaves application memory.
Resilient Data Pipeline: "Resilient JSON" parser that never fails on schema mismatches. It extracts maximum utility from AI output and wraps it in a clean status/payload envelope.
Cloud Native Integration:
Firestore (Native Mode): Real-time incident storage for responder dashboards
Cloud Storage: Persists raw "messy evidence" (images/audio) with immutable URLs
Text-to-Speech: Converts Hinglish summaries into audible instructions for accessibility



### 🚀 Google Cloud Deployment (Production Guide)
## 🔌Phase 1: Environment Preparation
Enable required APIs:
```Bash
gcloud services enable run.googleapis.com \
    cloudbuild.googleapis.com \
    firestore.googleapis.com \
    storage.googleapis.com \
    texttospeech.googleapis.com \
    secretmanager.googleapis.com
```
## 🏗️ Infrastructure Setup
📂 Firestore
Create a Firestore database in:
Mode: Native
Region: asia-south1 (Mumbai)

🪣 Cloud Storage Bucket
Create a storage bucket for media assets:
```bash
gsutil mb -l asia-south1 gs://project-setu-media
```

## Phase 2: IAM & Security Configuration
Assign roles to the Cloud Run service account:
```bash
gcloud projects add-iam-policy-binding [PROJECT_ID] \
    --member="serviceAccount:[SERVICE_ACCOUNT]" \
    --role="roles/datastore.user"

gcloud projects add-iam-policy-binding [PROJECT_ID] \
    --member="serviceAccount:[SERVICE_ACCOUNT]" \
    --role="roles/storage.objectAdmin"

gcloud projects add-iam-policy-binding [PROJECT_ID] \
    --member="serviceAccount:[SERVICE_ACCOUNT]" \
    --role="roles/cloudtts.admin"
```
## 🚀 Phase 3: Deploy to Cloud Run

Use the following command to deploy your application to **Google Cloud Run**:

```bash
gcloud run deploy project-setu \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated \
  --clear-base-image \
  --set-env-vars GOOGLE_API_KEY=[YOUR_KEY],GOOGLE_CLOUD_PROJECT=[YOUR_ID],GS_BUCKET_NAME=project-setu-media
```    

## ✅Phase 4: Post-Deployment Verification

👉 Health Check: https://[URL]/health

👉 UI: https://[URL]/ (High-contrast Setu form)

👉 API Docs: https://[URL]/docs


### 🔗 Live Deployment
👉 Deployed Link: https://project-setu-xxxxxxxx.asia-south1.run.app
