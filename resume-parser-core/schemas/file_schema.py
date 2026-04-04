from pydantic import BaseModel, Field

from core.workflows.models.resume import (
    Resume as BaseResume,
)
from core.workflows.models.resume import (
    WorkExperience as BaseWorkExperience,
)
from schemas.base_schema import BaseResponseModel


class YOE(BaseModel):
    year: int
    month: int


class WorkExperience(BaseWorkExperience):
    duration: YOE = Field(
        ..., description="The duration of the work experience in years and months."
    )


class Resume(BaseResume):
    work_experiences: list[WorkExperience] = Field(
        default_factory=list, description="The list of work experiences."
    )
    yoe: YOE = Field(
        ..., description="The total years of experience in years and months."
    )


class MarkdownResponseModel(BaseModel):
    filename: str = Field(..., description="The name of the file.")
    response: str = Field(..., description="The markdown representation of the resume.")


class ParseResponse(BaseModel):
    filename: str = Field(..., description="The name of the file.")
    markdown: str = Field(..., description="The markdown representation of the resume.")
    output: Resume = Field(
        ..., description="The structured output of the resume parsing."
    )


class ParseResponseModel(BaseResponseModel):
    response: ParseResponse
