from fastapi import UploadFile, HTTPException
from google.genai import types
from langsmith.run_helpers import traceable
from core.utils.pydantic_to_schema import pydantic_to_schema
from core.models.resume import Resume
from core.models.response import Response
from core.llm import client
from core.config import get_logger
from core.utils.pdf_utils import get_context

logger = get_logger(__name__)


@traceable(run_type="llm")
async def convert_to_markdown(file: UploadFile) -> str:
    try:
        logger.info("Converting %s to markdown...", file.filename)

        content = await file.read()
        user_message = "Identify whether the provided file is a resume or not. If it is a resume, convert this resume to markdown. Do not add or make up any information that is unavailable on the resume."

        if file.content_type == "application/pdf":
            # Get hyperlinks from the PDF file as additional context
            context = get_context(content)
            if context != "":
                user_message += context

        response = await client.aio.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=[
                types.Part.from_bytes(data=content, mime_type=file.content_type),
                types.Part.from_text(text=user_message),
            ],
            config=types.GenerateContentConfig(
                system_instruction="Follow user instruction carefully and answer with the provided schema.",
                temperature=0,
                max_output_tokens=8192,
                top_p=0.95,
                seed=0,
                response_mime_type="application/json",
                response_schema=pydantic_to_schema(Response.model_json_schema()),
            ),
        )

        if response.parsed["is_resume"] is False:
            logger.info("The file %s is not a resume.", file.filename)
            raise HTTPException(status_code=422, detail="The file is not a resume.")

        logger.info("Successfully converted %s to markdown.", file.filename)
        return response.parsed["resume_markdown"]
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Error converting PDF to markdown.")
    finally:
        await file.close()
        # logger.debug("Closed the file %s.", file.filename)


@traceable(run_type="llm")
async def convert_markdown_to_resume(markdown: str) -> dict:
    try:
        logger.info("Converting markdown to resume...")

        response = await client.aio.models.generate_content(
            model="gemini-exp-1206",
            contents=[
                types.Part.from_text(
                    f"Parse this resume markdown into structured format. Do not add or make up any information that is unavailable from the markdown. For non-required fields, if the information is not available, you can leave them blank. The resume markdown is below:\n\n{markdown}"
                ),
            ],
            config=types.GenerateContentConfig(
                system_instruction="Follow user instruction carefully and answer with the provided schema.",
                temperature=0,
                max_output_tokens=8192,
                top_p=0.95,
                seed=0,
                response_mime_type="application/json",
                response_schema=pydantic_to_schema(Resume.model_json_schema()),
            ),
        )

        logger.info("Successfully converted markdown to resume.")
        return response.parsed
    except Exception as e:
        logger.exception(e)
        raise HTTPException(
            status_code=500, detail="Error converting markdown to resume."
        )
