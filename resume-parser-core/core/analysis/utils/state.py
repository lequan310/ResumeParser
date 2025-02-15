from typing import TypedDict
from core.models.analysis import AnalysisResult


class InputState(TypedDict):
    resume: str
    job_desc: str


class State(TypedDict):
    resume: str
    requirements: str


class OutputState(TypedDict):
    result: AnalysisResult
