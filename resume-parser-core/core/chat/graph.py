from psycopg_pool import AsyncConnectionPool
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import HumanMessage, AIMessageChunk
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from langgraph.graph import StateGraph, START, END
from core.config import os
from core.chat.utils.state import State
from core.chat.utils.nodes import (
    tool_node,
    call_model,
    summarize_conversation,
    should_continue,
)


class ChatGraph:
    async def __init__(self):
        async with AsyncConnectionPool(
            # Example configuration
            conninfo=os.getenv("DB_URI"),
            max_size=20,
            kwargs={
                "autocommit": True,
                "prepare_threshold": 0,
            },
        ) as pool:
            # Create the graph
            graph = StateGraph(state_schema=State)

            # Create checkpointer
            checkpointer = AsyncPostgresSaver(pool)
            await checkpointer.setup()

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
            self._chatflow = graph.compile(checkpointer=checkpointer)

    async def ainvoke(self, input: dict, config: RunnableConfig = None):
        return await self._chatflow.ainvoke(input, config=config)

    async def astream(self, input: str, config: RunnableConfig = None):
        """Stream LLM responses for the conversation"""

        async for msg, metadata in self._chatflow.astream(
            {"messages": HumanMessage(content=input)},
            stream_mode="messages",
            config=config,
        ):
            if (
                msg.content
                and isinstance(msg, AIMessageChunk)
                and metadata["langgraph_node"] == "call_model"
            ):
                yield msg.content


chat_graph = ChatGraph()
