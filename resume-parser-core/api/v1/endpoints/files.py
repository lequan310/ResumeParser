from typing import Annotated
from fastapi import APIRouter, File, UploadFile, HTTPException
from schemas.file_schema import MarkdownResponseModel, ParseResponseModel
from services.file_service import FileService

file_service = FileService()
router = APIRouter(prefix="/files", tags=["Files"])


@router.post("/markdown", response_model=MarkdownResponseModel)
async def convert_markdown_single(file: Annotated[UploadFile, File()]):
    """Convert resume file to markdown.

    Args:
        file (UploadFile): Resume file. Defaults to File(...).

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
async def parse_resume(file: Annotated[UploadFile, File()]):
    """Parse Resume file into structured data.

    Args:
        file (UploadFile): Resume file. Defaults to File(...).

    Raises:
        HTTPException: Support only PDF and Image files

    Returns:
        response: OutputState
    """

    if file.content_type != "application/pdf":
        raise HTTPException(status_code=415, detail="Only PDF files are supported.")

    response = await file_service.parse_resume(file=file)

    return ParseResponseModel(response=response)
