from pydantic import BaseModel
from typing import Optional


class JobDesc(BaseModel):
    is_job_desc: bool
    basic_requirements: Optional[list[str]]
    preferred_requirements: Optional[list[str]]
