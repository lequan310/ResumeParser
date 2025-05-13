from langgraph.graph import StateGraph, START, END
from core.workflows.analysis.utils.state import State, OutputState, InputState
from core.workflows.analysis.utils.nodes import (
    extract_job_requirements,
    compare_resume_jd,
)


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
