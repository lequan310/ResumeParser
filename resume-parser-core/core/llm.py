import os
from google import genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from core.config import get_logger


logger = get_logger(__name__)

try:
    # Create the GenAI client for resume parsing
    client = genai.client.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    # LLMs for chatbot
    deepseek_llm = ChatGroq(
        model="deepseek-r1-distill-llama-70b",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=3,
        streaming=True,
    )

    llama_llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=3,
        streaming=True,
    )

    gemini_llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=3,
    )
except Exception as e:
    logger.exception(e)
    raise Exception("Error creating GenAI client.")
