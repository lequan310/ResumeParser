from typing import TypedDict

from fastapi import UploadFile


class InputState(TypedDict):
    input: UploadFile


class State(TypedDict):
    filename: str
    markdown: str
    output: dict
