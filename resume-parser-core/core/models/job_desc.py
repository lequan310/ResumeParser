from pydantic import BaseModel
from typing import Optional


class JobDesc(BaseModel):
    is_resume: bool
    basic_requirements: Optional[list[str]]
    preferred_requirements: Optional[list[str]]
