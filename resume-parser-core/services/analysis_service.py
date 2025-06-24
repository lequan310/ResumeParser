from core.workflows.analysis.graph import AnalysisGraph
from services.base_service import BaseService


class AnalysisService(BaseService):
    """
    Service class for handling analysis-related operations.
    """

    def __init__(self, graph: AnalysisGraph = None):
        """
        Initialize the analysis service.
        """

        if graph is None:
            graph = AnalysisGraph()

        self.analysis_graph = graph

        super().__init__(graph=graph)

    async def analyze(self, resume: str, job_desc: str):
        """
        Analyze the resume and job description.

        Args:
            resume (str): The resume text.
            job_desc (str): The job description text.

        Returns:
            dict: The analysis result.
        """

        result = await self.analysis_graph.ainvoke(
            {"resume": resume, "job_desc": job_desc}
        )

        return result["result"]
