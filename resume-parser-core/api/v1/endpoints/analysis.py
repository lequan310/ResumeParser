from fastapi import APIRouter, Body
from schemas.analysis_schema import AnalysisRequestModel, AnalysisResponseModel
from services.analysis_service import AnalysisService
from typing import Annotated


analysis_service = AnalysisService()
router = APIRouter(prefix="/analysis", tags=["Analysis"])


@router.post("", response_model=AnalysisResponseModel)
async def get_analysis(input: Annotated[AnalysisRequestModel, Body()]):
    result = await analysis_service.analyze(
        resume=input.resume, job_desc=input.job_desc
    )

    return AnalysisResponseModel(response=result)
