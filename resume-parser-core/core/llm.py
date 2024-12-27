from google import genai
from core.config import os

# Create the GenAI client
client = genai.client.Client(api_key=os.getenv("GOOGLE_API_KEY"))
