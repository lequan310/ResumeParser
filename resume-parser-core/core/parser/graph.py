from langgraph.graph import StateGraph, START, END
from core.config import get_logger
from core.parser.utils.state import InputState, State
from core.parser.utils.nodes import (
    get_resume_markdown,
    get_resume_structured,
    postprocess_resume_output,
)


class ParserGraph:
    def __init__(self):
        # Create the graph
        graph = StateGraph(state_schema=State, input=InputState, output=State)

        # Add nodes
        graph.add_node("get_resume_markdown", get_resume_markdown)
        graph.add_node("get_resume_structured", get_resume_structured)
        graph.add_node("postprocess_resume_output", postprocess_resume_output)

        # Add edges
        graph.add_edge(START, "get_resume_markdown")
        graph.add_edge("get_resume_markdown", "get_resume_structured")
        graph.add_edge("get_resume_structured", "postprocess_resume_output")
        graph.add_edge("postprocess_resume_output", END)

        # Compile the graph
        self._graph = graph.compile()

    async def ainvoke(self, input: dict):
        return await self._graph.ainvoke(input)


parser_graph = ParserGraph()
