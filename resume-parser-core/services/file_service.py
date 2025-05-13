from fastapi import UploadFile
from services.base_service import BaseService
from core.workflows.parser.graph import ParserGraph
from core.workflows.parser.utils.parse_utils import convert_to_markdown


class FileService(BaseService):
    """
    Service class for handling file-related operations.
    """

    def __init__(self, graph: ParserGraph = None):
        """
        Initialize the file service.
        """

        if graph is None:
            graph = ParserGraph()

        self.parser_graph = graph

        super().__init__(graph=graph)

    async def convert_to_markdown(self, file: UploadFile) -> str:
        """
        Convert a resume file to markdown.

        Args:
            file (str): The resume file.

        Returns:
            str: The converted markdown text.
        """

        return await convert_to_markdown(file=file)

    async def parse_resume(self, file: UploadFile):
        """
        Parse a resume file into structured data.

        Args:
            file (str): The resume file.

        Returns:
            dict: The parsed resume data.
        """

        response = await self.parser_graph.ainvoke({"input": file})

        return response
