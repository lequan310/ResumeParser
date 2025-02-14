from langgraph.graph import StateGraph, START, END
from core.analysis.utils.state import State, OutputState


class AnalysisGraph:
    def __init__(self):
        # Create the graph
        graph = StateGraph(state_schema=State, input=State, output=OutputState)

        # Add nodes

        # Add edges

        # Compile the graph
        self._graph = graph.compile()

    async def ainvoke(self, input: dict):
        return await self._graph.ainvoke(input)
