from fastapi import APIRouter, File, UploadFile
import pymupdf

router = APIRouter(prefix="/files", tags=["Files"])


@router.post("/convert_markdown")
async def convert_markdown(file: UploadFile = File(...)):
    """
    Convert an upload file into markdown.
    """

    pass
