from google import genai
from core.config import os, get_logger

logger = get_logger(__name__)

try:
    # Create the GenAI client
    client = genai.client.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    logger.info("GenAI client created successfully.")
except Exception as e:
    logger.exception(e)
    raise Exception("Error creating GenAI client.")
