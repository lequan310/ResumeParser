from fastapi import APIRouter, File, UploadFile, HTTPException
from core.parser.graph import ParserGraph
from core.parser.utils.parse_utils import convert_to_markdown

parser_graph = ParserGraph()
router = APIRouter(prefix="/files", tags=["Files"])


@router.post("/markdown")
async def convert_markdown_single(file: UploadFile = File(...)):
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
    response = await convert_to_markdown(file=file)

    return {"response": response}


@router.post("/resume")
async def parse_resume(file: UploadFile = File(...)):
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

    response = await parser_graph.ainvoke({"input": file})

    return {"response": response}
