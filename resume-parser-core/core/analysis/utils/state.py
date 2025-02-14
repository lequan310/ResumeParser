from typing import TypedDict
from core.models.analysis import AnalysisResult


class State(TypedDict):
    markdown: str
    job_desc: str


class OutputState(TypedDict):
    result: AnalysisResult
