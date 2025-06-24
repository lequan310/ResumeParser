from typing import Annotated

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, Depends

from core.container import Container
from schemas.analysis_schema import AnalysisRequestModel, AnalysisResponseModel
from services.analysis_service import AnalysisService

router = APIRouter(prefix="/analysis", tags=["Analysis"])


@router.post("", response_model=AnalysisResponseModel)
@inject
async def get_analysis(
    input: Annotated[AnalysisRequestModel, Body()],
    analysis_service: Annotated[
        AnalysisService, Depends(Provide[Container.analysis_service])
    ],
):
    """
    Get analysis of resume against job description.

    Args:
        input: Analysis request containing resume and job description
        analysis_service: Injected analysis service dependency

    Returns:
        AnalysisResponseModel: Analysis results
    """
    result = await analysis_service.analyze(
        resume=input.resume, job_desc=input.job_desc
    )

    return AnalysisResponseModel(response=result)
