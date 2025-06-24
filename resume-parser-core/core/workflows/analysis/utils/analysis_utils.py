from datetime import datetime

from fastapi import HTTPException
from google.genai import types
from langsmith.run_helpers import traceable

from core.workflows.llm import client
from core.workflows.models.analysis import AnalysisResult
from core.workflows.models.job_desc import JobDesc
from utils.logger_utils import get_logger
from utils.pydantic_to_schema import pydantic_to_schema

logger = get_logger(__name__)
job_desc_schema = pydantic_to_schema(JobDesc.model_json_schema())
analysis_result_schema = pydantic_to_schema(AnalysisResult.model_json_schema())


def format_md_string(string: str) -> str:
    """Format the string to markdown format.

    Args:
        string (str): input string

    Returns:
        str: formatted string
    """
    if string.startswith("```") and string.endswith("```"):
        return string
    return f"```\n{string}\n```"


@traceable(run_type="llm")
async def get_job_requirements(job_desc: str) -> dict:
    try:
        user_message = f"""Identify whether the provided text is a job description or not. If it is a job description, extract the requirements from the job description. Do not add or make up any information that is unavailable in the job description. Below is the provided text for your reference:\n\n{format_md_string(job_desc)}"""

        logger.info("Extracting job requirements...")

        response = await client.aio.models.generate_content(
            model="gemini-2.0-flash",
            contents=types.Part.from_text(text=user_message),
            config=types.GenerateContentConfig(
                system_instruction="Follow user instruction carefully and answer with the provided schema.",
                temperature=0,
                max_output_tokens=8192,
                top_p=0.95,
                seed=0,
                response_mime_type="application/json",
                response_schema=job_desc_schema,
            ),
        )

        if response.parsed["is_job_desc"] is False:
            raise HTTPException(
                status_code=422, detail="The provided text is not a job description."
            )

        logger.info("Successfully extract job requirements.")
        return response.parsed
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.exception(e)
        raise HTTPException(
            status_code=500, detail="Error extracting job requirements."
        )


@traceable(run_type="llm")
async def get_analysis_result(resume: str, job_requirements: str) -> dict:
    try:
        user_message = (
            "You are provided with a resume to compare against the job requirements. For each requirement, you must think and analyze carefully and then identify whether the resume meets the requirement or not."
            "\n\nThe result for each analysis can be:"
            "\n- 'YES' (the resume PARTIALLY OR FULLY meets the requirement)"
            "\n- 'UNCONFIRMED' (requires manual human screening to confirm)"
            "\n- 'NO' (the resume shows no sign of meeting the requirement)."
            f"\n\nBelow are the job requirements for your reference:\n\n{format_md_string(job_requirements)}"
            f"\n\nBelow is the resume for your reference:\n\n{format_md_string(resume)}"
        )

        today = datetime.today()
        formatted_date = f"{today.strftime('%B')} {today.day}, {today.year}"
        response = await client.aio.models.generate_content(
            model="gemini-2.5-flash-preview-04-17",
            contents=types.Part.from_text(text=user_message),
            config=types.GenerateContentConfig(
                system_instruction=f"You are a recruitment assistant. Follow user instruction carefully and answer with the provided schema. Note that the current date is {formatted_date} for reference purpose.",
                temperature=0,
                max_output_tokens=8192,
                top_p=0.95,
                seed=0,
                response_mime_type="application/json",
                response_schema=analysis_result_schema,
            ),
        )

        logger.info("Successfully analysed the resume against job description.")
        return response.parsed
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Error extracting analysis result.")
