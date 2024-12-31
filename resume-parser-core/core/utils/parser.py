from fastapi import UploadFile, HTTPException
from google.genai import types
from langsmith.run_helpers import traceable
from core.llm import client
from core.config import get_logger

logger = get_logger(__name__)


@traceable(run_type="chain")
async def convert_pdf_to_markdown(file: UploadFile) -> str:
    try:
        logger.info("Converting %s to markdown...", file.filename)

        content = await file.read()
        response = await client.aio.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=[
                types.Part.from_bytes(data=content, mime_type=file.content_type),
                types.Part.from_text(
                    "Convert this resume to markdown. Do not add any information that is unavailable on the resume."
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
