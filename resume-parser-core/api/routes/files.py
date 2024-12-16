import pymupdf
from fastapi import APIRouter, File, UploadFile, HTTPException
from core.utils.parser import convert_pdf_to_markdown

router = APIRouter(prefix="/files", tags=["Files"])


@router.post("/pdf_to_markdown")
async def convert_markdown_single(file: UploadFile = File(...)):
    """Convert an upload file into markdown."""

    if file.content_type != "application/pdf":
        raise HTTPException(status_code=415, detail="Only PDF files are supported.")

    # Convert from file to markdown
    response = await convert_pdf_to_markdown(file=file)

    return {"response": response}
