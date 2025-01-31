import json
from langchain_core.messages import (
    SystemMessage,
    ToolMessage,
    RemoveMessage,
    AIMessage,
    HumanMessage,
)
from langchain_core.runnables import RunnableConfig
from core.llm import gemini_llm
from core.agent import deepseek_agent
from core.chat.utils.tools import tools_by_name
from core.chat.utils.state import State
from core.chat.utils.prompts import DEEPSEEK_SYSTEM_MESSAGE
from core.config import get_logger

MAX_CONVERSATION_LENGTH = 10

logger = get_logger(__name__)


async def tool_node(state: State, config: RunnableConfig):
    """Call the tools with the arguments provided in the last message"""

    outputs = []
    logger.info(f"Calling tools. Thread ID: {config["configurable"]["thread_id"]}")
    for tool_call in state["messages"][-1].tool_calls:
        tool_result = await tools_by_name[tool_call["name"]].ainvoke(tool_call["args"])
        outputs.append(
            ToolMessage(
                content=json.dumps(tool_result),
                name=tool_call["name"],
                tool_call_id=tool_call["id"],
            )
        )
    return {"messages": outputs}


async def call_model(
    state: State,
    config: RunnableConfig,
):
    """Call the model with the system prompt and the conversation history"""

    summary = state.get("summary", "")
    if summary.strip() != "":
        context = f"Summary of conversation earlier: {summary}"
        system_prompt = SystemMessage(content=f"{DEEPSEEK_SYSTEM_MESSAGE}\n\n{context}")
    else:
        system_prompt = SystemMessage(content=DEEPSEEK_SYSTEM_MESSAGE)

    logger.info(f"Calling model. Thread ID: {config["configurable"]["thread_id"]}")
    response = await deepseek_agent.ainvoke([system_prompt] + state["messages"])
    return {"messages": [response]}


async def summarize_conversation(state: State, config: RunnableConfig):
    """Summarize the conversation so far when length of conversation reaches a certain point"""

    # Get the last 5 AI messages in the conversation (excluding messages with tool calls)
    ai_messages = [
        message
        for message in state["messages"]
        if isinstance(message, AIMessage) and not message.tool_calls
    ]

    if len(ai_messages) <= MAX_CONVERSATION_LENGTH:
        return

    summary = state.get("summary", "")
    if summary.strip() != "":
        # If a summary already exists, we use a different system prompt
        # to summarize it than if one didn't
        summary_instruction = (
            f"This is summary of the conversation to date: {summary}\n\n"
            "Extend the summary by taking into account the new messages above. Include only the summary when replying."
        )
    else:
        summary_instruction = "Create a concise summary of the conversation above. Include only the summary when replying."

    message_id = ai_messages[-2].id
    summary_messages = []

    # Find the index of the 5th AI message in the conversation using its id
    for message in state["messages"]:
        summary_messages.append(message)
        if message.id == message_id:
            break

    # Call the model to summarize the conversation
    logger.info(
        f"Summarizing conversation. Thread ID: {config["configurable"]["thread_id"]}"
    )
    summary = await gemini_llm.ainvoke(
        summary_messages + [HumanMessage(content=summary_instruction)]
    )
    removed_messages = [RemoveMessage(id=message.id) for message in summary_messages]
    return {"summary": summary.content, "messages": removed_messages}


def should_continue(state: State):
    """Conditional edge to check if agent needs to use tools"""

    messages = state["messages"]
    last_message = messages[-1]

    # If there is no function call, then we finish
    if not last_message.tool_calls:
        return "end"

    # Otherwise if there is, we continue
    else:
        return "continue"
