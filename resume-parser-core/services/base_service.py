from langgraph.graph.state import CompiledStateGraph


class BaseService:
    """
    Base class for all services.
    """

    def __init__(self, graph: CompiledStateGraph):
        """
        Initialize the base service.
        """

        self._graph = graph
