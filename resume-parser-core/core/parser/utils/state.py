from typing import TypedDict
from fastapi import UploadFile
from core.models.resume import Resume


class InputState(TypedDict):
    input: UploadFile


class State(TypedDict):
    markdown: str
    structured: Resume


class OutputState(TypedDict):
    structured: Resume
    output: dict
