# Replace the old line with these specific imports
from google.cloud import firestore
from google.cloud import storage
from google.cloud import secretmanager
import os

class GoogleSetuServices:
    def __init__(self):
        # Explicitly set the project ID if testing locally
        project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
        self.db = firestore.Client(project=project_id)
        self.storage_client = storage.Client(project=project_id)
        self.bucket = self.storage_client.bucket(os.getenv("GS_BUCKET_NAME", "project-setu-media"))

    def save_incident(self, incident_id, data):
        """Saves the bridge result to Firestore (Database Service)"""
        doc_ref = self.db.collection(u'incidents').document(incident_id)
        doc_ref.set(data)

    def upload_media(self, incident_id, file_bytes, filename):
        """Uploads messy evidence to Cloud Storage (Storage Service)"""
        blob = self.bucket.blob(f"evidence/{incident_id}_{filename}")
        blob.upload_from_string(file_bytes)
        return blob.public_url

def get_secret_api_key():
    """Retrieves API Key from Secret Manager (Security Parameter)"""
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{os.getenv('GOOGLE_CLOUD_PROJECT')}/secrets/GEMINI_API_KEY/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")