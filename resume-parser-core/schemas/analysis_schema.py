from pydantic import Field

from core.workflows.models.analysis import AnalysisResult
from schemas.base_schema import BaseRequestModel, BaseResponseModel


class AnalysisRequestModel(BaseRequestModel):
    resume: str = Field(..., description="The resume markdown to be analyzed.")
    job_desc: str = Field(..., description="The job description text.")


class AnalysisResponseModel(BaseResponseModel):
    response: AnalysisResult = Field(
        ..., description="The analysis result containing the score and feedback."
    )
