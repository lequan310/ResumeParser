from langgraph.graph import END, START, StateGraph

from core.workflows.analysis.utils.nodes import (
    compare_resume_jd,
    extract_job_requirements,
)
from core.workflows.analysis.utils.state import InputState, OutputState, State


class AnalysisGraph:
    def __init__(self):
        # Create the graph
        graph = StateGraph(state_schema=State, input=InputState, output=OutputState)

        # Add nodes
        graph.add_node("extract_job_requirements", extract_job_requirements)
        graph.add_node("compare_resume_jd", compare_resume_jd)

        # Add edges
        graph.add_edge(START, "extract_job_requirements")
        graph.add_edge("extract_job_requirements", "compare_resume_jd")
        graph.add_edge("compare_resume_jd", END)

        # Compile the graph
        self._graph = graph.compile()

    async def ainvoke(self, input: dict):
        return await self._graph.ainvoke(input)
