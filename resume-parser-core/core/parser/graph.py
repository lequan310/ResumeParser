from langgraph.graph import StateGraph, START, END


class ParserGraph:
    def __init__(self):
        graph = StateGraph()
        self._graph = graph.compile()

    async def ainvoke(self, input: dict):
        return await self._graph.ainvoke(input)
