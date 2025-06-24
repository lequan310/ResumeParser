from typing import Optional

from pydantic import BaseModel


class Response(BaseModel):
    is_resume: bool
    resume_markdown: Optional[str]
