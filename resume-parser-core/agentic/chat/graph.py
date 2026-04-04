from langchain_core.messages import AIMessageChunk, HumanMessage
from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from langgraph.graph import END, START, StateGraph

from agentic.chat.utils.nodes import (
    call_model,
    should_continue,
    summarize_conversation,
    tool_node,
)
from agentic.chat.utils.state import State
from core.db import get_connection_pool
from utils.logger_utils import get_logger

logger = get_logger(__name__)


class ChatGraph:
    def __init__(self):
        # Initialize _chatflow to None
        self._chatflow = None

    async def setup(self):
        try:
            # Create the graph
            graph = StateGraph(state_schema=State)

            # Create checkpointer
            self._checkpointer = AsyncPostgresSaver(get_connection_pool())
            await self._checkpointer.setup()

            # Add nodes
            graph.add_node("tool_node", tool_node)
            graph.add_node("call_model", call_model)
            graph.add_node("summarize_conversation", summarize_conversation)

            # Add edges
            graph.add_edge(START, "summarize_conversation")
            graph.add_edge("summarize_conversation", "call_model")
            graph.add_conditional_edges(
                "call_model",
                should_continue,
                {"continue": "tool_node", "end": END},
            )
            graph.add_edge("tool_node", "call_model")

            # Compile the graph
            self._chatflow = graph.compile(checkpointer=self._checkpointer)
        except Exception as e:
            logger.exception(e)
            raise RuntimeError(f"Failed to setup chat graph: {str(e)}")

    async def ainvoke(self, input: dict, config: RunnableConfig = None):
        if self._chatflow is None:
            raise RuntimeError("ChatGraph not properly initialized. Call setup() first")

        return await self._chatflow.ainvoke(input, config=config)

    async def astream(self, input: str, config: RunnableConfig = None):
        """Stream LLM responses for the conversation"""

        if self._chatflow is None:
            raise RuntimeError("ChatGraph not properly initialized. Call setup() first")

        async for msg, metadata in self._chatflow.astream(
            {"messages": HumanMessage(content=input)},
            stream_mode="messages",
            config=config,
        ):
            if (
                isinstance(msg, AIMessageChunk)
                and msg.content
                and metadata["langgraph_node"] == "call_model"
            ):
                yield msg.content

    async def cleanup(self, thread_id: str):
        """Cleanup the checkpoints from the thread id"""
        if self._checkpointer is not None:
            await self._checkpointer.adelete_thread(thread_id=thread_id)
