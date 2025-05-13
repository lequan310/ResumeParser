from pydantic import BaseModel
from typing import Optional


class Response(BaseModel):
    is_resume: bool
    resume_markdown: Optional[str]
