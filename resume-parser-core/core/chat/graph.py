from langgraph.graph import StateGraph, START, END
from langgraph.pregel import RetryPolicy


class ChatGraph:
    def __init__(self):
        # Create the graph
        graph = StateGraph()

        # Compile the graph
        self._graph = graph.compile()

    async def ainvoke(self, input: dict):
        return await self._graph.ainvoke(input)


chat_graph = ChatGraph()
