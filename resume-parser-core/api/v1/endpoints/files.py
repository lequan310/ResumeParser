from typing import Annotated

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from core.container import Container
from schemas.file_schema import MarkdownResponseModel, ParseResponseModel
from services.file_service import FileService

router = APIRouter(prefix="/files", tags=["Files"])


@router.post("/markdown", response_model=MarkdownResponseModel)
@inject
async def convert_markdown_single(
    file: Annotated[UploadFile, File()],
    file_service: FileService = Depends(Provide[Container.file_service]),
):
    """Convert resume file to markdown.

    Args:
        file (UploadFile): Resume file. Defaults to File(...).
        file_service (FileService): Injected file service dependency.

    Raises:
        HTTPException: Support only PDF and Image files

    Returns:
        response: str
    """

    if file.content_type != "application/pdf":
        raise HTTPException(status_code=415, detail="Only PDF files are supported.")

    # Convert from file to markdown
    markdown = await file_service.convert_to_markdown(file=file)

    return MarkdownResponseModel(filename=file.filename, response=markdown)


@router.post("/resume", response_model=ParseResponseModel)
@inject
async def parse_resume(
    file: Annotated[UploadFile, File()],
    file_service: Annotated[FileService, Depends(Provide[Container.file_service])],
):
    """Parse Resume file into structured data.

    Args:
        file (UploadFile): Resume file. Defaults to File(...).
        file_service (FileService): Injected file service dependency.

    Raises:
        HTTPException: Support only PDF and Image files

    Returns:
        response: OutputState
    """

    if file.content_type != "application/pdf":
        raise HTTPException(status_code=415, detail="Only PDF files are supported.")

    response = await file_service.parse_resume(file=file)

    return ParseResponseModel(response=response)
