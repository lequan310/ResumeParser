from core.config import os
from google import genai

# Create the GenAI client
client = genai.client.AsyncClient(
    api_client=genai.client.ApiClient(api_key=os.getenv("GOOGLE_API_KEY"))
)
