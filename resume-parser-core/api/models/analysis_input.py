from pydantic import BaseModel


class AnalysisInput(BaseModel):
    resume: str
    job_desc: str
