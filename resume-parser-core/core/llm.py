import google.generativeai as genai
import os


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(
    "gemini-2.0-flash-exp",
    generation_config={"temperature": 0, "max_output_tokens": None},
)
