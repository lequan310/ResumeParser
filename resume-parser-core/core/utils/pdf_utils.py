from pymupdf import open
from core.config import get_logger


logger = get_logger(__name__)


def get_links_from_pdf(file: bytes) -> list:
    """Get hyperlinks from the PDF file.

    Args:
        file (bytes): file stream

    Returns:
        list: list of hyperlinks
    """
    try:
        all_links = []

        # Open the PDF file using PyMUPDF
        with open(stream=file, filetype="pdf") as doc:
            # Get hyperlinks from the PDF file
            if doc.has_links():
                for page in doc:
                    links = [link["uri"] for link in page.get_links()]
                    all_links += links

        return all_links
    except Exception as e:
        logger.exception(e)
        return []


def get_context(file: bytes) -> str:
    """Get additional context from the PDF file.

    Args:
        file (bytes): file stream

    Returns:
        str: additional string context for concatenation
    """
    context = ""
    all_links = get_links_from_pdf(file)
    all_links_concat = "\n".join(all_links)

    if len(all_links) > 0:
        context = (
            "Additional Context: This file contains the following hyperlinks:\n"
            + all_links_concat
            + "\n\nInclude this information in the resume markdown conversion."
        )

    return context
