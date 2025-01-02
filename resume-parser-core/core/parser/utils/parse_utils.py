from fastapi import UploadFile, HTTPException
from google.genai import types
from langsmith.run_helpers import traceable
from core.utils.pydantic_to_schema import pydantic_to_schema
from core.models.resume import Resume
from core.llm import client
from core.config import get_logger

logger = get_logger(__name__)


@traceable(run_type="llm")
async def convert_to_markdown(file: UploadFile) -> str:
    try:
        logger.info("Converting %s to markdown...", file.filename)

        content = await file.read()
        response = await client.aio.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=[
                types.Part.from_bytes(data=content, mime_type=file.content_type),
                types.Part.from_text(
                    "Convert this resume to markdown. Do not add or make up any information that is unavailable on the resume."
                ),
            ],
            config=types.GenerateContentConfig(
                system_instruction="Follow user instruction carefully and answer in markdown format.",
                temperature=0,
                max_output_tokens=8192,
                top_p=0.95,
                seed=0,
            ),
        )

        logger.info("Successfully converted %s to markdown.", file.filename)
        return response.text
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Error converting PDF to markdown.")
    finally:
        await file.close()
        logger.debug("Closed the file %s.", file.filename)


@traceable(run_type="llm")
async def convert_markdown_to_resume(markdown: str) -> dict:
    try:
        logger.info("Converting markdown to resume...")

        resume_schema = pydantic_to_schema(Resume.model_json_schema())
        response = await client.aio.models.generate_content(
            model="gemini-exp-1206",
            contents=[
                types.Part.from_text(
                    f"Convert this resume to markdown. Do not add or make up any information that is unavailable from the markdown.\n\n{markdown}"
                ),
            ],
            config=types.GenerateContentConfig(
                system_instruction="Follow user instruction carefully and answer with the provided schema.",
                temperature=0,
                max_output_tokens=8192,
                top_p=0.95,
                seed=0,
                response_mime_type="application/json",
                response_schema=resume_schema,
            ),
        )

        logger.info("Successfully converted markdown to resume.")
        return response.parsed
    except Exception as e:
        logger.exception(e)
        raise HTTPException(
            status_code=500, detail="Error converting markdown to resume."
        )
