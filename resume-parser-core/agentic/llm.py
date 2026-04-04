from google import genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

from core.config import settings
from utils.logger_utils import get_logger

logger = get_logger(__name__)

try:
    # Create the GenAI client for resume parsing
    client = genai.client.Client(api_key=settings.GOOGLE_API_KEY)

    # LLMs for chatbot
    deepseek_llm = ChatGroq(
        model="openai/gpt-oss-120b",
        api_key=settings.GROQ_API_KEY,
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=3,
        streaming=True,
    )

    llama_llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=settings.GROQ_API_KEY,
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=3,
        streaming=True,
    )

    gemini_llm_default = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite-preview",
        api_key=settings.GOOGLE_API_KEY,
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=3,
    )
    gemini_llm = gemini_llm_default.bind_tools([{"google_search": {}}])
except Exception as e:
    logger.exception(e)
    raise Exception("Error creating GenAI client.")
