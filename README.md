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
graph LR
    subgraph "A. Agentic Development & Tuning"
        AS[Google AI Studio] -- "Prompt Prototyping" --> AG[Antigravity IDE]
        AG -- ".antigravity/rules.md" --> DE[Agentic Code Refinement]
        DE -- "Model Quantization/Tuning" --> GC[Gemini 1.5/2.0 Flash]
    end

    subgraph "B. Multimodal Ingestion Layer"
        UI[FastAPI / Jinja2 UI] --> SEC[PII Redactor: Regex/Logic]
        SEC -- "Sanitized Payload" --> BRIDGE[main.py: SetuBridge]
    end

    subgraph "C. Reasoning & Processing (The Bridge)"
        BRIDGE -- "Singleton Session" --> GC
        GC -- "Resilient JSON Parsing" --> PARSE[Data Transformer]
    end

    subgraph "D. Cloud Native Persistence & Aux"
        PARSE --> FS[(Cloud Firestore: NoSQL)]
        PARSE --> GCS[Cloud Storage: Blob Persistence]
        PARSE --> TTS[Cloud Text-to-Speech: i18n]
    end

    subgraph "E. Actionable Egress"
        PARSE --> OUT[Structured JSON Action]
        OUT --> API[Third-Party Emergency APIs]
    end

    %% Data Flow Styling
    style AS fill:#f9f,stroke:#333,stroke-width:2px
    style AG fill:#bbf,stroke:#333,stroke-width:2px
    style GC fill:#dfd,stroke:#333,stroke-width:4px
    style FS fill:#ffd,stroke:#333,stroke-width:2px


2. Technical Writeup: Project Setu (सेतु)
I. Project Philosophy
Project Setu is engineered as a Universal Bridge to solve the "Impedance Mismatch" between human chaos and system structure. In the Indian societal context, emergency data is rarely clean; it is multimodal, vernacular, and high-entropy. Setu uses a Reasoning-over-Parsing approach to transform this chaos into machine-interoperable actions.
II. Agentic Engineering with Antigravity & AI Studio
The intelligence of Setu was developed using a dual-loop AI feedback system:
Google AI Studio: Used for rapid prototyping of system instructions. We leveraged the multimodal playground to test how the model handles blurry Indian medical prescriptions versus noisy Hindi audio transcripts.
Antigravity IDE: The application code was refined using Antigravity’s agentic capabilities. We implemented an .antigravity/ configuration directory containing rules.md and architecture.md. These files instructed the Antigravity agents to maintain a Singleton Pattern for Gemini initialization and a Zero-Strictness Pydantic Model to ensure the bridge never crashes during high-stakes data ingestion.
III. Core Architectural Pillars
Multimodal Reasoning Engine: Utilizing Gemini 1.5/2.0 Flash via the v1beta API. The Flash model was selected for its high tokens-per-second (TPS) and low latency, essential for life-saving triage.
PII Sanitization (The Shield): A pre-processing layer in core/security.py redacts sensitive Indian identifiers (Aadhaar, PAN, Mobile) using optimized regex patterns. This ensures Data Privacy Compliance before the payload leaves the application memory.
Resilient Data Pipeline: The system uses a "Resilient JSON" parser. Instead of failing on schema mismatches, the parser extracts the maximum possible utility from the AI's output, wrapping "messy" data into a professional status/payload API envelope.
Cloud Native Integration:
Firestore (Native Mode): Stores real-time incident documents for responder dashboards.
Cloud Storage: Persists "Messy Evidence" (images/audio) with immutable URLs.
Text-to-Speech: Addresses the Accessibility Gap by converting Hinglish summaries into audible instructions for non-literate or visually impaired users.
3. Google Cloud Deployment Steps (Production Guide)
To deploy Project Setu to a production-grade Google Cloud Run environment, follow these technical steps:
Phase 1: Environment Preparation
Enable APIs:
code
Cmd
gcloud services enable run.googleapis.com cloudbuild.googleapis.com firestore.googleapis.com storage.googleapis.com texttospeech.googleapis.com secretmanager.googleapis.com
Create Infrastructure:
Firestore: Create a database in Native Mode in asia-south1.
Storage: Create a bucket: gsutil mb -l asia-south1 gs://project-setu-media.
Phase 2: IAM & Security Configuration
Assign necessary roles to the Cloud Run Service Account (e.g., [PROJECT_NUMBER]-compute@developer.gserviceaccount.com):
code
Cmd
gcloud projects add-iam-policy-binding [PROJECT_ID] \
    --member="serviceAccount:[SERVICE_ACCOUNT]" \
    --role="roles/datastore.user"

gcloud projects add-iam-policy-binding [PROJECT_ID] \
    --member="serviceAccount:[SERVICE_ACCOUNT]" \
    --role="roles/storage.objectAdmin"

gcloud projects add-iam-policy-binding [PROJECT_ID] \
    --member="serviceAccount:[SERVICE_ACCOUNT]" \
    --role="roles/cloudtts.admin"
Phase 3: Deployment via Cloud SDK
Execute the deployment from the root directory of project-setu. This command builds the container via Cloud Build and deploys it to the Mumbai region.
code
Cmd
gcloud run deploy project-setu ^
  --source . ^
  --region asia-south1 ^
  --allow-unauthenticated ^
  --clear-base-image ^
  --set-env-vars GOOGLE_API_KEY=[YOUR_KEY],GOOGLE_CLOUD_PROJECT=[YOUR_ID],GS_BUCKET_NAME=project-setu-media
Phase 4: Post-Deployment Verification
Health Check: https://[URL]/health (Confirm google_services: Enabled).
Accessible UI: https://[URL]/ (Confirm the high-contrast Red Setu form appears).
API Docs: https://[URL]/docs (Perform a multimodal crash test).
4. Deployed Link (Cloud Run URL)
Live Infrastructure: https://project-setu-32372428108.asia-south1.run.app
Project Setu is now a fully observable, secure, and accessible bridge for societal benefit, ready for large-scale Indian deployment.
