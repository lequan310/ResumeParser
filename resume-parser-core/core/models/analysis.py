from enum import Enum
from pydantic import BaseModel


class IsPresent(Enum):
    YES = "YES"
    UNCONFIRMED = "UNCONFIRMED"
    NO = "NO"


class RequirementCheck(BaseModel):
    requirement: str
    is_present: IsPresent


class AnalysisResult(BaseModel):
    basic_requirement_checks: list[RequirementCheck]
    preferred_requirement_checks: list[RequirementCheck]
