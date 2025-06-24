from typing import Optional

from pydantic import BaseModel


class JobDesc(BaseModel):
    is_job_desc: bool
    basic_requirements: Optional[list[str]]
    preferred_requirements: Optional[list[str]]
