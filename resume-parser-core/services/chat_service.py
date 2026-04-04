from agentic.chat.graph import ChatGraph
from services.base_service import BaseService


class ChatService(BaseService):
    """
    Service class for handling chat-related operations.
    """

    def __init__(self, graph: ChatGraph = None):
        """
        Initialize the chat service.
        """

        if graph is None:
            graph = ChatGraph()

        self.chat_graph = graph

        super().__init__(graph=graph)

    async def setup(self):
        """
        Setup the chat service.
        """

        await self.chat_graph.setup()

    async def send_message(self, message: str, thread_id: str):
        """
        Send a message to the chat service.

        Args:
            message (str): The message to send.
            thread_id (str): The ID of the chat thread.

        Returns:
            dict: The response from the chat service.
        """

        async for chunk in self.chat_graph.astream(
            input=message,
            config={"configurable": {"thread_id": thread_id}},
        ):
            yield chunk

    async def clear_history(self, thread_id: str):
        """
        Clear the chat history for a given thread.

        Args:
            thread_id (str): The ID of the chat thread.

        Returns:
            dict: The response from the chat service.
        """

        await self.chat_graph.cleanup(thread_id=thread_id)
